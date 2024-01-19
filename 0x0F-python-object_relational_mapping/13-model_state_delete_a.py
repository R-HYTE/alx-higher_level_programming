#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a' \
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_states_with_a(username, password, database):
    """
    Deletes all State objects with a name containing 'a' \
    from the specified database
    """
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

        # Query states whose names contain 'a'
        states_with_a = (
                session.query(State)
                .filter(State.name.like('%a%'))
                .all()
        )

        # Delete the states from the session
        for state in states_with_a:
            session.delete(state)

        # Commit the changes to the database
        session.commit()

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
    delete_states_with_a(username, password, database)
