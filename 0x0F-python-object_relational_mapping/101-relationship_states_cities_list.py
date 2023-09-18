#!/usr/bin/python3
"""
This script creates a connection to a MySQL database and
lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    conn_str = (f"mysql+mysqldb://{sys.argv[1]}"
                f":{sys.argv[2]}@localhost:3306/{sys.argv[3]}")
    engine = create_engine(conn_str, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        states = session.query(State).all()
        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"    {city.id}: {city.name}")
