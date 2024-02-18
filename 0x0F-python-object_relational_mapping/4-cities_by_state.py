#!/usr/bin/python3

# Write a script that lists all cities from the database
# This will be requiring Table Joining

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Get the Command line arguments
    _, username, password, dbName = sys.argv

    # Make connection to the database with MySQLdb module
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=dbName)

    # Get the cursor object from the db
    cur = db.cursor()

    # Execute your query on the cursor object
    cur.execute("SELECT cities.id, cities.name, states.name\
    FROM states JOIN cities ON states.id = cities.state_id")

    results = cur.fetchall()

    # Print the data returned
    for tup in results:
        print(tup)
