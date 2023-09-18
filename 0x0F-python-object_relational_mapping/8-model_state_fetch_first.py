#!/usr/bin/python3
"""
This script creates a connection to a MySQL database and prints
the first State object from the database hbtn_0e_6_usa and their IDs.
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

    with Session(engine) as session:
        state = session.query(State).order_by(State.id).first()

        if state:
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")
