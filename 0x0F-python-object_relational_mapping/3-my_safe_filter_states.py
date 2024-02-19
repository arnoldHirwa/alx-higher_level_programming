#!/usr/bin/python3
""" Lists values in the states tables of a database
where name matches the argument, and
that is safe from MySQL injections"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s;", (sys.argv[4],))
    states = cur.fetchall()
    for state in states:
        print(state)
