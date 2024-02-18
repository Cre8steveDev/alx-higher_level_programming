#!/usr/bin/python3
""" Write a script that lists all states from the
database hbtn_0e_0_usa"""
# import the sys module to access command line
# and the MySQLdb module

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Retrieve arguments from the command line
    _, username, password, dbName = sys.argv

    # Connect to the MySQL Server if on local host or to remote machine
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=dbName)
    # Retrieve cursor from the db instance
    cur = db.cursor()

    # Execute a MySQL Command on the cursor object
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Use the fetchall method on the cursor to retrieve the results
    result = cur.fetchall()

    # Print result to see output
    for tup in list(result):
        print(tup)
