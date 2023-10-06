import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('./instance/ERP-.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS USERS (
                    email TEXT PRIMARY KEY,
                    password TEXT NOT NULL,
                    status TEXT NOT NULL
                )''')

# users = ('admin@gmail.com', 'admin', 'A')
# users = ('anilkadu@gmail.com', 'teacher', 'T')
# users = ('varshadange@gmail.com', 'teacher', 'T')
# users = ('adityafukate@gmail.com', 'student', 'S')
# users = ('siddhantgaikwad@gmail.com', 'student', 'S')

# Insert data into the table
# cursor.execute("INSERT INTO USERS (email, password, status) VALUES (?, ?, ?)", users)

# Commit the changes to the database
# conn.commit()

# Query the database
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()

cursor.execute("SELECT * FROM users WHERE email=? AND password=?", ("admin@gmail.com", "admin"))
result = cursor.fetchone()

# Print the results
print(result)
# Close the cursor and the connection
cursor.close()
conn.close()
