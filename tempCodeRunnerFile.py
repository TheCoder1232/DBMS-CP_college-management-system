cursor.execute(f"SELECT studentID, {session.get('loginInfo')[5]} FROM ATTENDANCE WHERE CLASS=?", (selectedClass,))
        results=cursor.fetchall()