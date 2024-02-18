#!/usr/bin/python3

# # Write a script that lists all cities from the database
# # This will be requiring Table Joining
#
# if __name__ == "__main__":
#     import sys
#     import MySQLdb
#
#     # Get the Command line arguments
#     _, username, password, dbName = sys.argv
#
#     # Make connection to the database with MySQLdb module
#     db = MySQLdb.connect(host='localhost', port=3306, user=username,
#                          passwd=password, db=dbName)
#
#     # Get the cursor object from the db
#     cur = db.cursor()
#
#     # Execute your query on the cursor object
#     cur.execute("SELECT cities.id, cities.name, states.name\
#     FROM states INNER JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC")
#
#     results = cur.fetchall()
#
#     # Print the data returned
#     for tup in results:
#         print(tup)
#
#     cur.close()
#     db.close()

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

