#!/usr/bin/python3
"""
a script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    try:
        dbs = MySQLdb.connect(
                host="localhost", port=3306, user=argv[1],
                passwd=argv[2], db=argv[3]
                )
        cur = dbs.cursor()

        cur.execute("SELECT * FROM states WHERE name
                    LIKE BINARY 'N%' ORDER BY id")

        out = cur.fetchall()

        for row in out:
            print(row)

        cur.close()
        dbs.close()

    except MySQLdb.Error as e:
        print("My SQL Error:", e)
