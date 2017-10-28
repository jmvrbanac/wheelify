import argparse
import os
import subprocess
import sys

DEFAULT_WHEEL_DIR = os.path.join(os.environ['HOME'], '.manylinux')
PYTHON_VERSION_MAP = {
    'python2.7': 'cp27-cp27mu',
    'python3.6': 'cp36-cp36m',
}


def is_linux():
    return sys.platform == "linux" or sys.platform == "linux2"


def get_user_id(username):
    stdout = subprocess.check_output(f'id -u {username}', shell=True)
    return stdout.decode('utf-8').strip()


def requires_sudo():
    groups = subprocess.check_output('groups').decode('utf-8').split()
    return 'root' not in groups and 'docker' not in groups


def build(requirements_file, output_dir, username, python):
    os.makedirs(output_dir, exist_ok=True)

    pip = f'/opt/python/{python}/bin/pip'
    user_id = get_user_id(username)
    sudo = 'sudo ' if is_linux() and requires_sudo() else ''

    build_cmd = (
        f'useradd -u {user_id} {username}; '
        f'{pip} wheel -f /io/wheels -w /io/wheels -r /io/requirements.txt; '
        f'chown -R {username}:{username} /io/wheels'
    )

    cmd = (
        f'{sudo}docker run -it --rm --env BUILD_USER={username} '
        f'--env USER_ID=`id -u {username}` '
        f'-v {requirements_file}:/io/requirements.txt '
        f'-v {output_dir}:/io/wheels quay.io/pypa/manylinux1_x86_64 '
        f'/bin/bash -c "{build_cmd}"'
    )

    return subprocess.run(cmd, shell=True)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description='wheelify - Manylinux builder'
    )

    parser.add_argument('requirements_file', type=str)
    parser.add_argument('--user', type=str, default=os.environ['USER'])
    parser.add_argument('--wheel-dir', type=str, default=DEFAULT_WHEEL_DIR)
    parser.add_argument(
        '--python',
        type=str,
        choices=PYTHON_VERSION_MAP.keys(),
        default='python3.6'
    )

    args = parser.parse_args(argv)

    build(
        requirements_file=os.path.abspath(args.requirements_file),
        output_dir=args.wheel_dir,
        username=args.user,
        python=PYTHON_VERSION_MAP[args.python]
    )
