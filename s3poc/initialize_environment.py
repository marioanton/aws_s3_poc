#!/usr/bin/env python
from s3poc.resources import initialise
from s3poc.interfaces.database import mysql
def go():
    # read from environment variables or key vault or similar.
    # verifies params are passed properly.
    print("Initializing environemnt")
    initialise.generate_images() # insert logic not to create images.
    # Create Databse
    print("Create Database")
    mysql.run_query("mysql", "CREATE DATABASE IF NOT EXISTS sketch")
    print("Create Table for image path")
    mysql.run_query("sketch", "CREATE TABLE IF NOT EXISTS image_path (name VARCHAR(20));")

