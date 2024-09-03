#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host='localhost',
                         user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    state_name = args[4]
    cur.execute("SELECT cities.name FROM cities JOIN \
                states ON cities.state_id=states.id \
                WHERE  states.name=%s  ORDER BY cities.id ASC", [state_name])
    cities = cur.fetchall()
    city_list = []
    for row in cities:
        city_list.append(row[0])
    print(", ".join(city_list))
