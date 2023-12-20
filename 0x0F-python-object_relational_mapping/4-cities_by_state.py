#!/usr/bin/python3
"""
Lists all cities
from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    cur.execute(
        """
        SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON states.id = cities.state_id \
        ORDER BY cities.id;
        """)
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()
