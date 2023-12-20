#!/usr/bin/python3
"""
Lists all states with a name
from user input (that is safe from sql injection)
from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    cur.execute(
        """
        SELECT * FROM states WHERE \
        CONVERT(name USING utf8mb4) COLLATE utf8mb4_0900_as_cs  = %s \
        ORDER BY id;
        """, (sys.argv[4], ))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
