'''
Implementing SQL statements and queries to perform additional operations
and using Python to execute the SQL statements.
'''

# Import dependencies
import sqlite3
import pathlib
import logging
import pandas as pd


# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')


# Define the database file path
db_file_path = pathlib.Path("project.db")

def execute_sql_from_file(db_filepath, sql_file):
    try:
        with sqlite3.connect(db_filepath) as conn:
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Executed SQL from {sql_file}")
            print(f"Executed SQL from {sql_file}")
    except (sqlite3.Error, FileNotFoundError) as e:
        error_message = f"Error executing SQL from {sql_file}: {e}"
        logging.error(error_message)
        print(error_message)

# Define SQL paths
def main():
    
    logging.info("Program started")
    sql_files = [
        pathlib.Path("sql").joinpath("delete_records.sql"),
        pathlib.Path("sql").joinpath("insert_records.sql"),
        pathlib.Path("sql").joinpath("query_aggregation.sql"),
        pathlib.Path("sql").joinpath("query_filter.sql"),
        pathlib.Path("sql").joinpath("query_group_by.sql"),
        pathlib.Path("sql").joinpath("query_join.sql"),
        pathlib.Path("sql").joinpath("query_sorting.sql"),
        pathlib.Path("sql").joinpath("update_records.sql")
    ]

    # Execute the files
    for sql_file in sql_files:
        execute_sql_from_file(db_file_path, sql_file)
        logging.debug("execute_sql_from_file")

    logging.info("Program ended")

if __name__ == "__main__":
    main()