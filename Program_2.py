# Author: Michael Beaudet
# Title: Week 13 Program 2
# Date: 5/2/25

import sqlite3

# Connect to the database (that doesn't exist)
conn = sqlite3.connect('cities.db')

# Create a cursor object to execute commands
cursor = conn.cursor()

# Create the Cities table, but it doesn't exist
# cursor.execute()

# Commit changes and close the connection
conn.commit()
conn.close()