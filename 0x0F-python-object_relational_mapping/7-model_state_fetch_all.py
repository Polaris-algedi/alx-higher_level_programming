#!/usr/bin/python3
"""
This script creates a connection to a MySQL database and prints
the states and their IDs.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    conn_str = (f"mysql+mysqldb://{sys.argv[1]}"
                f":{sys.argv[2]}@localhost:3306/{sys.argv[3]}")
    engine = create_engine(conn_str, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")

    session.close()
