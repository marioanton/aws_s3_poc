#!/usr/bin/env python
import sys
from s3poc.interfaces.authentication import auth_val
from s3poc.interfaces.database  import mysql
from . import initialize_environment

def main():
    sys.tracebacklimit = 0
    initialize_environment.go()
    auth_val.authentication() # i don't like this.

if __name__ == '__main__':
    main()
