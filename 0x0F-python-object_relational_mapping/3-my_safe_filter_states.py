#!/usr/bin/python3

"""Write a script that lists all states with a name starting
with N (Uppercase N) from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Get the Command line arguments
    _, username, password, dbName, searchName = sys.argv
    searchName = str(searchName)

    # Preventing possible SQL Injection using text validation
    # Check to ensure the user input is an alphanumeric character,
    # and it doesn't contain any special character

    if not searchName.isalnum():
        sys.exit()

    # Make connection to the database with MySQLdb module
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=dbName)

    # Get the cursor object from the db
    cur = db.cursor()

    # Execute your query on the cursor object
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY'{}' "
                "ORDER BY states.id ASC"
                .format(searchName))

    results = cur.fetchall()

    # Print the data returned
    for tup in results:
        print(tup)

    cur.close()
    db.close()
