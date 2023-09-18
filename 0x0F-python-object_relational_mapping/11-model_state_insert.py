#!/usr/bin/python3
"""
This script creates a connection to a MySQL database and adds
the State object “Louisiana” to the database hbtn_0e_6_usa
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

    with Session(engine) as session:
        louisiana = State(name="Louisiana")
        session.add(louisiana)
        session.commit()
        print(f"{louisiana.id}")
