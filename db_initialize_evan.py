# Import from Python Standard Library first
import sqlite3
import pathlib
import logging
import pandas as pd

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

# Define paths using joinpath
db_file_path = pathlib.Path("project.db")
sql_file_path = pathlib.Path("sql").joinpath("create_tables.sql")
author_data_path = pathlib.Path("data").joinpath("authors.csv")
book_data_path = pathlib.Path("data").joinpath("books.csv")

def verify_and_create_folders(paths):
    for path in paths:
        folder = path.parent
        if not folder.exists():
            print(f"Creating folder: {folder}")
            folder.mkdir(parents=True, exist_ok=True)
        else:
            print(f"Folder already exists: {folder}")

def create_database(db_path):
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating the database: {e}")

def create_tables(db_path, sql_file_path):
    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_file_path, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def insert_data_from_csv(db_path, author_data_path, book_data_path):
    try:
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_path) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"Error inserting data: {e}")

def main():

    logging.info("Program started")
    paths_to_verify = [sql_file_path, author_data_path, book_data_path]
    verify_and_create_folders(paths_to_verify)   
    logging.debug("create folders")
    create_database(db_file_path)
    logging.debug("create database")
    create_tables(db_file_path, sql_file_path)
    logging.debug("create tables")
    insert_data_from_csv(db_file_path, author_data_path, book_data_path)
    logging.debug("insert_data_from_csv")
    logging.info("Program ended")

if __name__ == "__main__":
    main()