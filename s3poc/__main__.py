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
            print('python -m s3poc -e "http://localhost:9000" -s "legacy" -d "production" -n "image" -o "avatar" ')
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

    # sys.tracebacklimit = 0
    # initialize_environment.go()
    # auth_val.authentication() # i don't like this.
    client = boto3.client(service_name="s3", use_ssl=False, endpoint_url=endpoint_url)
    # get_set_update.s3_set_object(client)
    # # get_set_update.s3_update_metadata(client)
    # # get_set_update.s3_get_bucket(client)
    get_set_update.s3_sync(endpoint_url, src_bucket, dst_bucket)
    result = mysql.run_query("sketch", "SELECT name from image_path where name like '%{0}/image%' limit 100" .format(old_key_path))
    prev_result = 0
    while len(result) > 0:
            prev_result = len(result)
            for row in result:
                legacy_key = row[0]
                production_key = row[0].replace(old_key_path, new_key_path)
                status = test.test_object("%s/%s" % (endpoint_url, legacy_key))
                if status == 200:
                    print("Renaming key for object %s" %production_key)
                    get_set_update.s3_object_rename(client, dst_bucket, legacy_key, production_key)
                status = test.test_object("%s/%s" % (endpoint_url, production_key))
                if status == 200:
                    print("Updating DB for object %s" %production_key)
                    mysql.run_update_query("sketch", "update image_path set name = REPLACE(name,'legacy','production') where name = '%s'"  %(legacy_key)) 
            result = mysql.run_query("sketch", "SELECT name from image_path where name like '%{0}/image%' limit 100" .format(old_key_path))
    if len(result) == prev_result and prev_result != 0:
       sys.exit("There is manual intervention required to finish off migration - Number of obejcts pending - %d" %prev_result) 
if __name__ == '__main__':
    main(sys.argv[1:])
