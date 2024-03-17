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

    query_rows = db_session.query(State).first()
    if query_rows is None:
        print("Nothing")
    print("{}: {}".format(query_rows.id, query_rows.name))
