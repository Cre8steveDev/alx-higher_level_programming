#!/usr/bin/python3

"""Write a script that lists all states with a name starting
with N (Uppercase N) from the database hbtn_0e_0_usa"""

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
    # the 'N%' is like a matching patter
    # saying "And any other possible combo of letters
    # cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%'")
    cur.execute("SELECT * FROM states ORDER BY states.id ASC \
    WHERE LEFT(states.name, 1) = 'N'")

    results = cur.fetchall()

    # Print the data returned
    for tup in results:
        print(tup)
