#!/usr/bin/python3
"""
    SQL Alchmy module, fetch all records
"""


from model_state import State, Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """
        create Engine and fecth all records from the table
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    db_session = Session()

    db_insert = State(name="Louisiana")
    db_session.add(db_insert)
    db_session.commit()
    print("{0}".format(db_insert.id))
    db_session.close()
