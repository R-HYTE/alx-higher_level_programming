#!/usr/bin/python3
"""Print the first State object from the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_first_state(username, password, database):
    """Prints the first State object from the specified database."""
    try:
        # Create a database engine
        # You can use the pool_pre_ping but you'll get a WARNING
        # - on it's deprecation
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
        )

        # Create the tables based on the defined models
        Base.metadata.create_all(engine)

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the first state and print its details
        state = session.query(State).order_by(State.id).first()
        if state:
            print("{}: {}".format(state.id, state.name))
        else:
            print("Nothing")

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    print_first_state(username, password, database)
