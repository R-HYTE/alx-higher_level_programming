#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

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

    # Query City objects and their corresponding states
    results = (
            session.query(City, State)
            .filter(City.state_id == State.id)
            .order_by(City.id).all()
    )

    # Print information about cities and states
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
