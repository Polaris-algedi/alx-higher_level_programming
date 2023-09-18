#!/usr/bin/python3
"""
This script creates a connection to a MySQL database and prints
the State object with the name passed as argument from
the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

if __name__ == "__main__":
    conn_str = (f"mysql+mysqldb://{sys.argv[1]}"
                f":{sys.argv[2]}@localhost:3306/{sys.argv[3]}")
    engine = create_engine(conn_str, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    state_name = sys.argv[4]

    try:
        with Session(engine) as session:
            state = session.query(State).filter(State.name == state_name).one()
            print(f"{state.id}")
    except NoResultFound:
        print("Not found")
