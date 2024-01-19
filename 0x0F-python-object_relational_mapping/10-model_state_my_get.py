#!/usr/bin/python3
"""Print the State object with the name passed as an argument"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def find_state_by_name(username, password, database, search_name):
    """Prints the State object with the specified name from the database."""
    try:
        # Create a database engine
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
            pool_pre_ping=True
        )

        # Create the tables based on the defined models
        Base.metadata.create_all(engine)

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the state by name
        state = session.query(State).filter(State.name == search_name).first()

        # Display the result
        if state:
            print("{}".format(state.id))
        else:
            print("Not found")

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> "
              "<database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, search_name = sys.argv[1], sys.argv[2], \
        sys.argv[3], sys.argv[4]
    find_state_by_name(username, password, database, search_name)
