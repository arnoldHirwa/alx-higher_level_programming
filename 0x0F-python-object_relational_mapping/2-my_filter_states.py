#!/usr/bin/python3
"""
Lists values in the states tables of a database where name
matches the argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    srch = sys.argv[4]
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()
    for st in states:
        if st[1] == srch:
            print(st)
