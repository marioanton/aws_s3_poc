from s3poc.interfaces.s3_api import auth
from s3poc.interfaces.database import mysql

def authentication ():
    auth.s3_auth_and_access()
    mysql.mysql_and_access()