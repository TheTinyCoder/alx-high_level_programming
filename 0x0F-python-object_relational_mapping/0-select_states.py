#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import sys
from MySQLdb import _mysql

if __name__ == '__main__':
    db = _mysql.connect(
        user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id""")
    states = cur.fetchmany()
    for state in states:
        print(state)
    cur.close()
    db.close()
