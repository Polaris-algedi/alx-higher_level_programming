#!/usr/bin/python3
"""
MySQL Database Query Script

This script connects to a MySQL database and retrieves
all states with a name starting with N (upper N) from the database.

Usage:
    python3 script.py <username> <password> <database_name>

Arguments:
    <username>: The MySQL username to connect with.
    <password>: The password for the MySQL user.
    <database_name>: The name of the database to connect to.

Example:
    python3 script.py myuser mypassword mydb

Requirements:
    - MySQLdb Python library must be installed.

"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
