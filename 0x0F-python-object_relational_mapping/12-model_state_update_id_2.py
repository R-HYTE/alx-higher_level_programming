#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def change_state_name(username, password, database):
    """Changes the name of a State object in the specified database."""
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

        # Query the state with ID 2
        state_to_update = session.query(State).filter(State.id == 2).first()

        # Check if the state with ID 2 exists
        if state_to_update:
            # Change the name of the state with ID 2 to "New Mexico"
            state_to_update.name = "New Mexico"

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
    change_state_name(username, password, database)
