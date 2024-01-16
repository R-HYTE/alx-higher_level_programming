#!/usr/bin/python3
"""
Script to list all cities from the hbtn_0e_4_usa database.

Usage: ./list_cities.py <username> <password> <database>
"""

import sys
import MySQLdb


def list_cities_by_state():
    """
    Connects to a MySQL server, and retrieves and displays all cities from
    the database along with their corresponding states.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()

    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id;
    """

    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    if db:
        db.close()


if __name__ == "__main__":
    list_cities_by_state()
