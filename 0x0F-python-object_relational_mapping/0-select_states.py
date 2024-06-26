#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    try:
        db = MySQLdb.connect(
                host="localhost", port=3306, user=argv[1],
                passwd=argv[2], db=argv[3]
                )
        cur = db.cursor()

        cur.execute("SELECT * FROM states")

        out = cur.fetchall()

        for row in out:
            print(row)

        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
