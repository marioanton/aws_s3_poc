#!/usr/bin/env python
import mysql.connector 
import sys

def auth_and_access():
    print("Authenticating with Mysql")
    # try to connect to mysql
    try:
        cnx = mysql.connector.connect(host="localhost", user="sketch", passwd="password", db="mysql")
        cursor = cnx.cursor(buffered=True) # https://stackoverflow.com/questions/29772337/python-mysql-connector-unread-result-found-when-using-fetchone
        cursor.execute("show variables")   # Syntax error in query
        cursor.close()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        sys.exit(1)

def run_query(database,query):
    # try to connect to mysql
    try:
        cnx = mysql.connector.connect(host="localhost", user="root", passwd="password", db=database)
        cursor = cnx.cursor(buffered=True)
        cursor.execute("%s"%(query))   # Syntax error in query
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        sys.exit(1)

def run_update_query(database,query):
    # try to connect to mysql
    try:
        cnx = mysql.connector.connect(host="localhost", user="root", passwd="password", db=database)
        cursor = cnx.cursor(buffered=True)
        cursor.execute("%s"%(query))   # Syntax error in query
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        sys.exit(1)
