#!/usr/bin/env python3
"""
Lists cities in a given state from a MySQL database.
"""

import MySQLdb
from sys import argv


def get_city_names_by_state(username, password, database, state_name):
    """
    Retrieves and prints the names of cities in the specified state.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
        state_name (str): Name of the state.

    Returns:
        None
    """
    try:
        # Establishing a database connection
        connection = MySQLdb.connect(host="localhost", port=3306,
                                     user=username, passwd=password,
                                     db=database, charset="utf8")

        # Creating a cursor for executing queries
        cursor = connection.cursor()

        # SQL query to retrieve city names in the specified state
        query = """
            SELECT cities.name FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """
        cursor.execute(query, (state_name,))

        # Fetching and printing the results
        city_names = [row[0] for row in cursor.fetchall()]
        print(", ".join(city_names))

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        # Closing cursor and database connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    # Checking if command-line arguments are provided
    if len(argv) != 5:
        print("Usage: python script.py <username> "
              "<password> <database> <state_name>")
    else:
        # Extracting command-line arguments
        script, username, password, database, state_name = argv

        # Calling the function to retrieve and print city names
        get_city_names_by_state(username, password, database, state_name)
