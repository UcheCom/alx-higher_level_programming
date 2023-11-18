#!/usr/bin/python3
""" Lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT c.name
                   FROM cities AS c
                   JOIN states AS s ON c.state_id = s.id
                   WHERE s.name = %s
                   ORDER BY c.id ASC;""", (sys.argv[4],))
    cities = cur.fetchall()
    cities = [city[0] for city in cities]
    print(", ".join(cities))
    cur.close()
    db.close()
