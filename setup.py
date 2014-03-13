#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup, Command
from subprocess import check_call
from os import path

try:
    from reinferio.proto import SetupProtoCompiler
except ImportError:
    import sys
    print("ERROR: setup.py depends on py-reinferio.proto in order to compile "
          "the proto files into a Python package - install it and try again",
          file=sys.stderr)
    sys.exit(1)

PROTO_PREFIX = '/usr/share/proto/reinferio'

PKG_NAME = 'pb_saltfish'
SetupProtoCompiler.pkg_name = PKG_NAME
SetupProtoCompiler.files = [('saltfish.proto', True)]
SetupProtoCompiler.deps = [path.join(PROTO_PREFIX, 'core.proto')]

setup(name='reinferio.' + PKG_NAME,
      version='0.1.0',
      description='reinfer.io core protos',
      author='reinfer.io Ltd.',
      author_email='marius@reinfer.io',
      url='https://github.com/reinferio/saltfish-proto.git',
      test_suite='test',
      install_requires=[
          'reinferio.proto>=0.1.0',
          'rpcz>=0.9',
      ],
      cmdclass={
          'compile': SetupProtoCompiler,
      },
      packages=[
          'reinferio',
          'reinferio.' + PKG_NAME,
      ],
      namespace_packages=[
          'reinferio'
      ]
     )
