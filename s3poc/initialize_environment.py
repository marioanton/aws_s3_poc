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
    mysql.run_query("mysql", "CREATE DATABASE  IF NOT EXISTS sketch")
    print("Create Table for image path")
    mysql.run_query("sketch", "DROP TABLE  IF EXISTS image_path")
    mysql.run_query("sketch", "DROP PROCEDURE myproc")
    mysql.run_query("sketch", "CREATE TABLE IF NOT EXISTS image_path (name varchar(50),image_name VARCHAR(20));")
    mysql.run_query("sketch", "CREATE PROCEDURE myproc() BEGIN DECLARE i int DEFAULT 0; WHILE i <= 1000 DO INSERT INTO image_path (name, image_name ) VALUES (CONCAT('legacy\/image',i,'.png'), 'dasd@i');SET i = i + 1; END WHILE;END")
    mysql.run_query("sketch", "CALL myproc")
