import os
import re

import pytest
from wheelify.app import main

test_requirements = '\n'.join([
    'pyyaml',
    'appdirs'
])


@pytest.fixture
def setup_tmp(tmpdir):
    build_dir = tmpdir.mkdir('build')

    requirements = build_dir.join('requirements.txt')
    requirements.write(test_requirements)

    return build_dir, str(requirements)


def test_wheel_building(setup_tmp):
    build_dir, requirements = setup_tmp
    wheel_dir = str(build_dir.join('wheels'))
    check_cmd = f'--wheel-dir {wheel_dir} {requirements}'

    main(check_cmd.split(' '))
    files = os.listdir(wheel_dir)

    assert re.fullmatch('appdirs.*py2.py3-none-any.whl', files[0])
    assert re.fullmatch('PyYAML.*cp36-cp36m-linux_x86_64.whl', files[1])
