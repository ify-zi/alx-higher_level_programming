#!/usr/bin/python3
"""
    ORM module - MYSQLdb
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
        connectto daabse and retrive a selected data
    """
    db_conn = MySQLdb.connect(host="localhost", port=3306,
                              user=argv[1], passwd=argv[2], db=argv[3])

    cur = db_conn.cursor()
    cur.execute("""SELECT cities.id, cities.name \
                FROM cities JOIN states \
                ON cities.state_id = states.id \
                WHERE states.name LIKE BINARY
                %(state_name)s
                ORDER BY cities.id \
                ASC""", {'state_name': argv[4]})
    query_rows = cur.fetchall()

    if query_rows is not None:
        print(", ".join([row[1] for row in query_rows]))

    cur.close()
    db_conn.close()
