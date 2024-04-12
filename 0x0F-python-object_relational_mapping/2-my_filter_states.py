#!/usr/bin/python3
"""
script thattakes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    try:
        db = MySQLdb.connect(
                host="localhost", port=3306, user=argv[1],
                passwd=argv[2], db=argv[3]
                )
        cur = db.cursor()

        state_name = argv[4]
        query = """
                SELECT *
                FROM states
                WHERE name = '{}'
                ORDER BY states.id ASC;
        """.format(state_name)

        cur.execute(query)

        out = cur.fetchall()

        for row in out:
            print(row)

        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
