#!/usr/bin/python3
""" Lists cities of a database """
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities INNER JOIN states \
                ON cities.state_id = states.id;")
    ct = cur.fetchall()
    for c in ct:
        print(c)
