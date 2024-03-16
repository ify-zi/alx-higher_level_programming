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
    cur.execute("SELECT * FROM states WHERE name \
                LIKE BINARY 'N%' ORDER BY states.id \
                ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db_conn.close()
