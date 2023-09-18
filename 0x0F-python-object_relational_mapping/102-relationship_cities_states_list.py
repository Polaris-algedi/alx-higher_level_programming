#!/usr/bin/python3
"""
This script creates a connection to a MySQL database and
lists all City objects from the database hbtn_0e_101_usa
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
        cities = session.query(City).all()
        for city in cities:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))
