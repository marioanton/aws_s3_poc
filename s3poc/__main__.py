#!/usr/bin/env python


def initialize_environment():
    # read from environment variables or key vault or similar.
    # verifies params are passed properly.
    print("Initializing environemnt")

from s3poc.interfaces.authentication import authentication_validation


if __name__ == '__main__':

    initialize_environment()
    authentication_validation.mysql_auth
    authentication_validation.s3_auth



