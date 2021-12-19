#!/usr/bin/python3
"""
Using the SQLAlchemy module, list all City objects and their corresponding
State name from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for row in session.query(City)\
                      .join(State)\
                      .filter(State.id == City.state_id)\
                      .order_by(City.id):
        print("{}: {} -> {}".format(row.id, row.name, row.state.name))
