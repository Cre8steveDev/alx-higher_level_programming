#!/usr/bin/python3

""" Write a script that takes in the name of a state as an argumetn
and lists all cities of that state using the database hbtn_0e_4_usa.

Your script should take 4 arguments: mysql username, mysql password,
database name and state name (SQL Injection free)"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Retrieve command line arguments
    if len(sys.argv) < 5:
        sys.exit()

    username, password, dbName, stateName = sys.argv[1:]

    # Validate user input from stateName
    if not str(stateName).isalnum():
        sys.exit()

    # Connect to MySQL Server
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         port=3306, db=dbName)

    # Get cursor from database connection
    cur = db.cursor()

    # Execute SQL Statement on the cursor
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (stateName,))

    # retrieve the result
    result: tuple = cur.fetchall()

    for idx, tup in enumerate(result):
        print(tup[0], end=("" if idx + 1 == len(result) else ", "))
    print()

    cur.close()
    db.close()
