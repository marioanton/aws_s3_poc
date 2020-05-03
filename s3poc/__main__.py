#!/usr/bin/env python
import sys
from s3poc.interfaces.authentication import auth_val
from s3poc.interfaces.database  import mysql
from s3poc.interfaces.s3_api import get_set_update
from s3poc.tests import test
import boto3
import getopt
from . import initialize_environment

def main(argv):

    endpoint_url = ''
    src_bucket = ''
    dst_bucket = ''

    try:
        opts, args = getopt.getopt(argv,"he:s:d:n:o:")
    except getopt.GetoptError:
        print('python -m s3poc -e <endpoint_url> -s <src_bucket> -d <dst_bucket> -n <new_key_path> -o <old_key_path> ')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python -m s3poc -e <endpoint_url> -s <src_bucket> -d <dst_bucket>')
            sys.exit()
        elif opt in ("-e"):
            endpoint_url = arg
        elif opt in ("-d"):
            dst_bucket = arg
        elif opt in ("-s"):
            src_bucket = arg
        elif opt in ("-n"):
            new_key_path = arg
        elif opt in ("-o"):
            old_key_path = arg

    print('Destination bucket is file is', endpoint_url)
    print('dst file is', dst_bucket)
    print('src file is', src_bucket)

    # sys.tracebacklimit = 0
    # initialize_environment.go()
    # auth_val.authentication() # i don't like this.
    client = boto3.client(service_name="s3", use_ssl=False, endpoint_url=endpoint_url)
    # get_set_update.s3_set_object(client)
    # # get_set_update.s3_update_metadata(client)
    # # get_set_update.s3_get_bucket(client)
    # get_set_update.s3_sync(endpoint_url, src_bucket, dst_bucket)
    total_records = 100
    while total_records > 99:
        result = mysql.run_query("sketch", "SELECT name from image_path where name like '%legacy%' limit 100")
        # insert while here.

        for row in result:
            legacy_key = row[0]
            production_key = row[0].replace(old_key_path, new_key_path)
            get_set_update.s3_object_rename(client, dst_bucket, legacy_key, production_key)
            status = test.test_object("%s/%s" % (endpoint_url, production_key))
            if status == 403:
                mysql.run_update_query("sketch", "update image_path set name = REPLACE(name,'legacy','production')" ) 
                # print(result)
                

if __name__ == '__main__':
    main(sys.argv[1:])
