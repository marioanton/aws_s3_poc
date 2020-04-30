#!/usr/bin/env python
from . import initialize_environment
from s3poc.interfaces.authentication import auth_val
import sys, traceback

def main():
    sys.tracebacklimit = 0
    initialize_environment.init()
    auth_val.authentication() # i don't like this 


if __name__ == '__main__':
    main()
