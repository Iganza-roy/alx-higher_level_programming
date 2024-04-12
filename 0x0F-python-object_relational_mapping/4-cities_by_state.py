#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
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

        query = """
                SELECT cities.id, cities.name, states.name\
                FROM cities\
                JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id;\
            """
        cur.execute(query)

        out = cur.fetchall()

        for res in out:
            print(res)


        cur.close()
        dbs.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
