#!/usr/bin/python3
'''
Script to search and display values in the states table of hbtn_0e_0_usa
where name matches the provided state name.

Usage: ./search_states.py <username> <password> <database> <state_name>
'''
import sys
import MySQLdb


def search_states():
    """
    Connects to a MySQL server and retrieves and displays rows
    from the states table where the state name matches the provided argument.
    """

    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id;"
                   .format(state_name))

    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the database connection
    db.close()


if __name__ == "__main__":
    search_states()
