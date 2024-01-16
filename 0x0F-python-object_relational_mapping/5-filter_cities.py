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
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id) AS city_list
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s;
    """
    cursor.execute(query, (state_name,))

    result = cursor.fetchone()

    if result and result[0]:
        city_list = result[0]
        print(city_list)
    else:
        print("No cities found for the state '{}'.".format(state_name))

    if db:
        db.close()


if __name__ == "__main__":
    filter_cities_by_state()
