#!/usr/bin/env python
import argparse
from subprocess import check_call
import sys

DEFAULT_PREFIX='/usr/share/proto/reinferio'
PROTO_FILE = 'saltfish.proto'

call = lambda cmd: check_call(
    cmd, shell=True, stdout=sys.stdout, stderr=sys.stderr)


call('mkdir -pv %s' % DEFAULT_PREFIX)
call('cp -uv %s %s' % (PROTO_FILE, DEFAULT_PREFIX))

parser = argparse.ArgumentParser()
parser.add_argument('--python', action='store_true',
    help='install python package in addtion to copying protos')
if parser.parse_args().python:
    call('./setup.py compile')
    call('./setup.py install')
