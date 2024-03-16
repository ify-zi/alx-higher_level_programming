#!/usr/bin/python3
"""
    ORM module
"""

import MySQLdb
import sys


db_conn = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

cur = db_conn.cursor()
cur.execute("SELECT * FROM states")
query_row = cur.fetchall()

for row in query_row:
    print(row)

cur.close()
db_conn.close()
