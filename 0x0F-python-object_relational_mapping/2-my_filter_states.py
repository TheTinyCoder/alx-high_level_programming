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
    query = "SELECT * FROM states WHERE name = '{}'".format(state)
    cur.execute(query)
    states = cur.fetchall()
    for row in states:
        print(row)
