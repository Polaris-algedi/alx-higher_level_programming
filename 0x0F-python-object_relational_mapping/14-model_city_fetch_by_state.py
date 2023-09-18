#!/usr/bin/python3
"""
This script creates a connection to a MySQL database and
prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    conn_str = (f"mysql+mysqldb://{sys.argv[1]}"
                f":{sys.argv[2]}@localhost:3306/{sys.argv[3]}")
    engine = create_engine(conn_str, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        cities = session.query(City, State).filter(City.state_id == State.id)\
                                     .order_by(City.id).all()
        for city, state in cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
