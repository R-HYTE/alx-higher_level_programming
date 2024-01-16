#!/usr/bin/python3
"""
Script to list all cities of a specific state from the hbtn_0e_4_usa database.

Usage: ./5-filter_cities.py <username> <password> <database> <state_name>
"""

import sys
import MySQLdb


def filter_cities_by_state():
    """
    Connects to a MySQL server and retrieves and displays all cities
    of a specific state from the database (SQL injection free).
    """
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()

    query = """
        SELECT * FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id;
    """
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()

    for row in results:
        print(row[2])  # Assuming the city name is in the third column

    if db:
        db.close()


if __name__ == "__main__":
    filter_cities_by_state()
