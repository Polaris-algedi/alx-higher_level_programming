#!/usr/bin/python3
"""
MySQL Database Query Script

This script connects to a MySQL database and retrieves all
values in the states table of hbtn_0e_0_usa where name matches the argument.
Usage:
    python3 script.py <username> <password> <database_name> <state_name>

Arguments:
    <username>: The MySQL username to connect with.
    <password>: The password for the MySQL user.
    <database_name>: The name of the database to connect to.
    <state_name>: The name of the state to search for.

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
    query = f"SELECT * FROM states WHERE name='{sys.argv[4]}' ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
