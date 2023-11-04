import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('./instance/ERP.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table
# cursor.execute('''CREATE TABLE IF NOT EXISTS ADMIN (
#                     adminID TEXT PRIMARY KEY NOT NULL,
#                     teacherID TEXT,
#                     studentID TEXT,
#                     email TEXT NOT NULL,
#                     password TEXT NOT NULL,
#                     phone TEXT NOT NULL,
#                     name TEXT NOT NULL,
#                     dob TEXT NOT NULL,
#                     address TEXT NOT NULL,
#                     FOREIGN KEY (studentID) REFERENCES STUDENT (studentID),
#                     FOREIGN KEY (teacherID) REFERENCES TEACHER (teacherID)
#                 )''')

# cursor.execute('''CREATE TABLE IF NOT EXISTS TEACHER (
#                     teacherID TEXT PRIMARY KEY NOT NULL,
#                     adminID TEXT,
#                     studentID TEXT,
#                     attendanceID TEXT,
#                     timetableID TEXT,
#                     subCode TEXT,
#                     email TEXT NOT NULL,
#                     password TEXT NOT NULL,
#                     name TEXT NOT NULL,
#                     dob TEXT NOT NULL,
#                     address TEXT NOT NULL,
#                     phone TEXT NOT NULL,
#                     yearsExp TEXT NOT NULL,
#                     FOREIGN KEY (adminID) REFERENCES ADMIN (adminID),
#                     FOREIGN KEY (studentID) REFERENCES STUDENT (studentID),
#                     FOREIGN KEY (attendanceID) REFERENCES ATTENDANCE (attendanceID),
#                     FOREIGN KEY (timetableID) REFERENCES TIMETABLE (timetableID),
#                     FOREIGN KEY (subCode) REFERENCES  EXAM (subCode)
#                 )''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENT (
#                     studentID TEXT PRIMARY KEY NOT NULL,
#                     timetableID TEXT,
#                     attendanceID TEXT,
#                     subCode TEXT,
#                     adminID TEXT,
#                     teacherID TEXT,
#                     email TEXT NOT NULL,
#                     password TEXT NOT NULL,
#                     name TEXT NOT NULL,
#                     rollNo TEXT NOT NULL,
#                     dob TEXT NOT NULL,
#                     address TEXT NOT NULL,
#                     phone TEXT NOT NULL,
#                     FOREIGN KEY (adminID) REFERENCES ADMIN (adminID),
#                     FOREIGN KEY (teacherID) REFERENCES TEACHER (teacherID),
#                     FOREIGN KEY (attendanceID) REFERENCES ATTENDANCE (attendanceID),
#                     FOREIGN KEY (timetableID) REFERENCES TIMETABLE (timetableID),
#                     FOREIGN KEY (subCode) REFERENCES  EXAM (subCode)
#                 )''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS TIMETABLE (
#                     timetableID TEXT PRIMARY KEY NOT NULL,
#                     teacherID TEXT,
#                     studentID TEXT,
#                     subCode TEXT NOT NULL,
#                     day TEXT NOT NULL,
#                     time TEXT NOT NULL,
#                     FOREIGN KEY (studentID) REFERENCES STUDENT (studentID),
#                     FOREIGN KEY (teacherID) REFERENCES TEACHER (teacherID)
#                 )''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS ATTENDANCE (
#                     attendanceID TEXT PRIMARY KEY NOT NULL,
#                     teacherID TEXT,
#                     studentID TEXT,
#                     rollNo TEXT NOT NULL,
#                     subCode TEXT NOT NULL,
#                     present TEXT NOT NULL,
#                     FOREIGN KEY (studentID) REFERENCES STUDENT (studentID),
#                     FOREIGN KEY (teacherID) REFERENCES TEACHER (teacherID)
#                 )''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS EXAM (
#                     subCode TEXT PRIMARY KEY NOT NULL,
#                     teacherID TEXT,
#                     studentID TEXT,
#                     date TEXT NOT NULL,
#                     marks TEXT NOT NULL,
#                     FOREIGN KEY (studentID) REFERENCES STUDENT (studentID),
#                     FOREIGN KEY (teacherID) REFERENCES TEACHER (teacherID)
#                 )''')

################################################################################


# Create the "ATTENDANCE" table with the specified columns
# cursor.execute("""
# CREATE TABLE ATTENDANCE (
#     studentID INTEGER PRIMARY KEY,
#     DBMS TEXT,
#     IOT TEXT,
#     OOP TEXT,
#     DSA TEXT,
#     DS TEXT,
#     POPL TEXT
# )
# """)
# cursor.execute("""
# INSERT INTO ATTENDANCE VALUES(12211371, "9/10", "4/6", "6/7", "6/10", "9/12", "2/10")
#  """)


# cursor.execute('''CREATE TABLE IF NOT EXISTS USERS (
#                     email TEXT PRIMARY KEY,
#                     password TEXT NOT NULL,
#                     status TEXT NOT NULL
#                 )''')

# users = ('admin@gmail.com', 'admin', 'A')
# users = ('anilkadu@gmail.com', 'teacher', 'T')
# users = ('varshadange@gmail.com', 'teacher', 'T')
# users = ('adityafukate@gmail.com', 'student', 'S')
# users = ('siddhantgaikwad@gmail.com', 'student', 'S')

# Insert data into the table
# cursor.execute("INSERT INTO USERS (email, password, status) VALUES (?, ?, ?)", users)

# Commit the changes to the database

# cursor.execute('''INSERT INTO ADMIN 
#                VALUES ('ADMIN', NULL, NULL, 'admin@gmail.com','admin', '9322857001', 'ADMIN!', '2004-05-17', 'PUNE,MAHARASHTRA')''')
# cursor.execute('select * from ADMIN')
# print('success')
# Execute the query to retrieve table names
# Close the database connection when done
conn.commit()


# Query the database
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()

# cursor.execute("SELECT * FROM users WHERE email=? AND password=?", ("admin@gmail.com", "admin"))
# result = cursor.fetchone()

# Print the results
# print(result)
# Close the cursor and the connection
cursor.close()
conn.close()
