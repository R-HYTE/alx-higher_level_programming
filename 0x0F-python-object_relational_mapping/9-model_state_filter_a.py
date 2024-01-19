#!/usr/bin/python3
"""List all State objects that contain the letter 'a'"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states_with_a(username, password, database):
    """Lists all State objects that contain the letter 'a'."""
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

        # Query and print states whose names contain 'a', ordered by id
        states = (
                session.query(State)
                .filter(State.name.like('%a%'))
                .order_by(State.id)
                .all()
        )

        # Display the results
        for state in states:
            print("{}: {}".format(state.id, state.name))

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
    list_states_with_a(username, password, database)
