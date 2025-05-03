# Author: Michael Beaudet
# Title: Week 13 Program 4
# Date: 5/2/25

import sqlite3

# Connect to the database (that doesn't exist)
conn = sqlite3.connect('phonebook.db')

# Create a cursor object to execute commands
cursor = conn.cursor()

# Create the phonebook table, but it doesn't exist
# cursor.execute()

# Commit changes and close the connection
conn.commit()
conn.close()