#!/usr/bin/env python
import sys
from s3poc.interfaces.authentication import auth_val
from s3poc.resources import generate
from . import initialize_environment

def main():
    sys.tracebacklimit = 0
    initialize_environment.init()
    auth_val.authentication() # i don't like this.

    generate.generate_images() # insert logic not to create images.

if __name__ == '__main__':
    main()
