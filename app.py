from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)
conn = sqlite3.connect('./instance/ERP.db', check_same_thread=False)
cursor = conn.cursor()
app.app_context().push()

#Login Function
@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method=="POST":
        email = request.form["login_email"]
        password = request.form["login_password"]

        cursor.execute("SELECT * FROM ADMIN WHERE email=? AND password=?", (email, password))
        result = cursor.fetchone()
        if result is not None:
            return render_template("AdminHomePage.html")
        
        cursor.execute("SELECT * FROM STUDENT WHERE email=? AND password=?", (email, password))
        result = cursor.fetchone()
        if result is not None:
            return render_template("StudentHomePage.html")
        
        cursor.execute("SELECT * FROM TEACHER WHERE email=? AND password=?", (email, password))
        result = cursor.fetchone()
        if result is not None:
            return render_template("TeacherHomePage.html")
    
        else:
            return render_template("login_page.html", exist=False)
    else:
        return render_template("login_page.html", exist=True)
    

#Admin Functions
@app.route("/AdminHomePage")
def AdminHomePage():
    return render_template("AdminHomePage.html")


@app.route("/AdminAddStudent", methods=['GET', 'POST'])
def AdminAddStudent():
    if request.method=="POST":
        StudentName=request.form["StudentName"]
        PNo=request.form["PNo"]
        Addr=request.form["Addr"]
        UID=request.form["UID"]
        RNo=request.form["RNo"]
        DOB=request.form["DOB"]
        Email=request.form["Email"]
        Password=request.form["Password"]
        try:
            insert_query = '''INSERT INTO STUDENT (studentID, timetableID, attendanceID, subCode, adminID, teacherID, email, password, name, rollNo, dob, address,phone)
               VALUES(?,?, ?, ?, ?, ?, ?, ?,?,?,?,?,?)'''
        # Execute the query using the cursor and pass the values as a tuple
            cursor.execute(insert_query, (UID,'timetableID','attendanceID','subCode','ADMIN','teacherID',Email,Password,StudentName,RNo,DOB,Addr,PNo))
            conn.commit()
            print('success')
            return render_template('AdminAddStudent.html' ,success=True)
        except:
            print('bruh')
            return render_template('AdminAddStudent.html' ,success=False)
    else:
        return render_template('AdminAddStudent.html')

@app.route("/AdminDeleteStudent" ,methods=['POST','GET'])
def AdminDeleteStudent():
    if request.method=="POST":
        DeleteForm=request.form.get('DeleteForm')
        if DeleteForm=='Search':
            uid=request.form["UID1"]
            cursor.execute('select * from STUDENT where studentID=?',(uid,))
            result=cursor.fetchone()
            if result is not None:
                return render_template('AdminDeleteStudent.html', result=result,exists=True)
            else:
                return render_template('AdminDeleteStudent.html', exists=False)
        if DeleteForm=='Confirm':
            cursor.execute('delete from STUDENT where studentID=?',(uid,))
            conn.commit()
            return render_template('AdminDeleteStudent.html',  exists='deleted')
    elif request.method=='GET':
        return render_template('AdminDeleteStudent.html', exists='nothing')
    else:
        return render_template('AdminDeleteStudent.html',exists='nothing')

        

       

@app.route("/AdminAddTeacher", methods=['POST','GET'])
def AdminAddTeacher():
    if request.method=="POST":
        TeacherName=request.form["TeacherName"]
        PNo=request.form["PNo"]
        Addr=request.form["Addr"]
        UID=request.form["UID"]
        EXP=request.form["EXP"]
        DOB=request.form["DOB"]
        SUBJ=request.form["SUBJ"]
        Email=request.form["Email"]
        Password=request.form["Password"]
        print('done')
        try:
            insert_query = '''INSERT INTO TEACHER (teacherID, adminID, studentID, attendanceID, timetableID, subCode, email, password, name, dob, address, phone, yearsExp)
               VALUES(?, ?, NULL, ?, ?, ?, ?, ?,?,?,?,?,?)'''
        # Execute the query using the cursor and pass the values as a tuple
            cursor.execute(insert_query, (UID,'ADMIN',  'attendanceID', 'timetableID', SUBJ, Email,Password, TeacherName, DOB, Addr,PNo,EXP))
            conn.commit()
            print('success')
            return render_template('AdminAddTeacher.html' ,success=True)
        except:
            print('bruh')
            return render_template('AdminAddTeacher.html' ,success=False)
    else:
        return render_template('AdminAddTeacher.html')

@app.route("/AdminDeleteTeacher" ,methods=['POST','GET'])
def AdminDeleteTeacher():
    if request.method=="POST":
        DeleteForm=request.form.get('DeleteForm')
        if DeleteForm=='Search':
            uid=request.form["UID1"]

            if uid=='1':
                #write query to get student values
                return render_template('AdminDeleteTeacher.html', exists=True)
            else:
                return render_template('AdminDeleteTeacher.html', exists=False)
        if DeleteForm=='Confirm':
            #write query to delete student values
            return render_template('AdminDeleteTeacher.html',  exists='deleted')
    elif request.method=='GET':
        return render_template('AdminDeleteTeacher.html', exists='nothing')
    else:
        return render_template('AdminDeleteTeacher.html',exists='nothing')


#Teacher Functions 
@app.route("/TeacherHomePage")
def TeacherHomePage():
    return render_template('TeacherHomePage.html')


#Student Functions
@app.route("/StudentHomePage")
def StudentHomePage():
    return render_template("StudentHomePage.html")

@app.route("/StudentAttendancePage")
def StudentAttendancePage():
    return render_template("StudentAttendancePage.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
