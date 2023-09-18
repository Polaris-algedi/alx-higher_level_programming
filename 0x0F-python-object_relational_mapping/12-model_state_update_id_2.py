#!/usr/bin/python3
"""
This script creates a connection to a MySQL database and
changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, update
from sqlalchemy.orm import Session

if __name__ == "__main__":
    conn_str = (f"mysql+mysqldb://{sys.argv[1]}"
                f":{sys.argv[2]}@localhost:3306/{sys.argv[3]}")
    engine = create_engine(conn_str, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        stmt = update(State).\
               where(State.id == 2).\
               values(name='New Mexico')

        session.execute(stmt)
        session.commit()
