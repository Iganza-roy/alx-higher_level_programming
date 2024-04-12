#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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

        state_name = argv[4]
        query = """
                SELECT cities.id, cities.name\
                FROM cities\
                JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id;\
            """
        cur.execute(query, (state_name,))

        out = cur.fetchall()

        cities_names = (', ').join(city[1] for city in out)
        print(cities_names)

        cur.close()
        dbs.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
