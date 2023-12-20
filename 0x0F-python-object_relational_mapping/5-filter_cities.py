#!/usr/bin/python3
"""
Filter cities by state name
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
        SELECT cities.name FROM cities \
        JOIN states ON states.id = cities.state_id \
        WHERE states.name = %s \
        ORDER BY cities.id;
        """, (sys.argv[4], ))
    cities = cur.fetchall()
    for index, city in enumerate(cities):
        print(city)
        if index < cities.length - 1:
            print(", ")
    cur.close()
    db.close()
