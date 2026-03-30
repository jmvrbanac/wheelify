Wheelify (Archived)
===================

**This project is no longer maintained.** See `Alternatives`_ below.

Wheelify was a small utility for building manylinux-compatible Python wheels
inside a controlled Docker environment. The original motivation was simple:
produce portable Linux wheels without manually constructing Docker invocations.

Why the build environment matters
----------------------------------

When you build a Python wheel, the base image you build *in* is part of your
supply chain. An outdated or untrusted base image can introduce known-vulnerable
system libraries baked into compiled extensions, and leaves no verifiable
provenance — no way to answer "what exactly ran during this build?"

Why it's archived
-----------------

The landscape shifted significantly since this was written in 2017:

- ``manylinux1`` is effectively dead. The PyPA images stopped receiving updates
  and modern pip rejects manylinux1 wheels on current glibc systems. The
  standard has moved to ``manylinux2014``, ``manylinux_2_28``, and
  ``musllinux``.
- Python 2.7 and 3.6, the only supported versions, are both end-of-life.
- No ARM support, which matters on Apple Silicon and AWS Graviton.
- The use case (wheels from a requirements file) is narrow, and better-maintained
  tools now cover the broader problem.

Alternatives
------------

- `cibuildwheel <https://cibuildwheel.pypa.io>`_ — the de facto standard for
  building wheels across Linux, macOS, and Windows, with multi-Python and
  multi-arch support. Use this.
- ``pip wheel -r requirements.txt`` with a current
  `PyPA manylinux image <https://github.com/pypa/manylinux>`_ if you want the
  manual Docker approach without a wrapper.

Original usage
--------------

.. code-block:: shell

    wheelify <requirements_file> [--user USER] [--wheel-dir WHEEL_DIR] [--python {python2.7,python3.6}]

License
-------

Apache 2.0
