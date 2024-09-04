#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])
    state = args[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s \
             COLLATE utf8mb4_0900_as_cs", [state])
    states = cur.fetchall()
    for row in states:
        print(row)