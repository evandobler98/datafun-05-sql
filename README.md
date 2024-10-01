# Module 5 Project - SQL

## Overview
This project is all about combining SQL into a Python project. This project uses SQLite, logging, imported CSV files, and multiple SQL operations to extract and manipulate data.

## Importing Dependencies
A requirements.txt file was created and listed the dependencies needed for this project. 
Packages were installed with the following command:
'''
python3 -m pip install -r requirements.txt
'''

## Commands Used 
'''
git add . 
git commit -m "message"
git push -u origin main
'''

## File Types
* .py - Python files
* .sql - SQL files
* .sqlite - SQLite files

## Create Database
The following code in which was used to create a database:

'''
import sqlite3
import pathlib
import logging
import pandas as pd

logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

db_file_path = pathlib.Path("project.db")
sql_file_path = pathlib.Path("sql").joinpath("create_tables.sql")
author_data_path = pathlib.Path("data").joinpath("authors.csv")
book_data_path = pathlib.Path("data").joinpath("books.csv")

def create_database(db_path):
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating the database: {e}")

if __name__ == "__main__":
    main()
'''


## Create Tables 
This code creates the "authors" and "books" tables. The "authors" table holds the primary key and the "books" table holds the foreign keys used to create the relation of tables. The following code was used to create the tables:

'''
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT,
    year_published INTEGER,
    author_id TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    year_born INTEGER
);
'''

