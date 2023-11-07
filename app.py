from flask import Flask, render_template, request, redirect, session
import sqlite3


app = Flask(__name__)
conn = sqlite3.connect('./instance/ERP.db', check_same_thread=False)
cursor = conn.cursor()
app.app_context().push()

app.secret_key = 'DBMS'
#Login Function
@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method=="POST":
        email = request.form["login_email"]
        password = request.form["login_password"]
       

        cursor.execute("SELECT * FROM ADMIN WHERE email=? AND password=?", (email, password))
        result = cursor.fetchone()
        session['loginInfo']=result
        if result is not None:
            return render_template("AdminHomePage.html",result=session.get('loginInfo'))
        
        cursor.execute("SELECT * FROM STUDENT WHERE email=? AND password=?", (email, password))
        result = cursor.fetchone()
        session['loginInfo']=result
        if result is not None:
            return render_template("StudentHomePage.html",result=session.get('loginInfo'))
        
        cursor.execute("SELECT * FROM TEACHER WHERE email=? AND password=?", (email, password))
        result = cursor.fetchone()
        session['loginInfo']=result
        if result is not None:
            return render_template("TeacherHomePage.html",result=session.get('loginInfo'))
    
        else:
            return render_template("login_page.html", exist=False)
    else:
        return render_template("login_page.html", exist=True)
    

#Admin Functions
@app.route("/AdminHomePage")
def AdminHomePage():
    
    return render_template("AdminHomePage.html",result=session.get('loginInfo'))


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
            session['uid'] = uid 
            cursor.execute('select * from STUDENT where studentID=?',(uid,))
            result=cursor.fetchone()
            if result is not None:
                return render_template('AdminDeleteStudent.html', result=result,exists=True)
            else:
                return render_template('AdminDeleteStudent.html', exists=False)
        if DeleteForm=='Confirm':
            uid = session.get('uid')
            if uid is not None:
                cursor.execute('delete from STUDENT where studentID=?',(uid,))
                conn.commit()
                print(uid)
                print("yes")
                return render_template('AdminDeleteStudent.html',result='NULL', exists='deleted')
            else:
                print('bruh')
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
            session['uid'] = uid 
            cursor.execute('select * from TEACHER where teacherID=?',(uid,))
            result=cursor.fetchone()
            if result is not None:
                return render_template('AdminDeleteTeacher.html', result=result,exists=True)
            else:
                return render_template('AdminDeleteTeacher.html', exists=False)
        if DeleteForm=='Confirm':
            uid = session.get('uid')
            if uid is not None:
                cursor.execute('delete from TEACHER where teacherID=?',(uid,))
                conn.commit()
                print(uid)
                print("yes")
                return render_template('AdminDeleteTeacher.html',result='NULL', exists='deleted')
            else:
                print('bruh')
    elif request.method=='GET':
        return render_template('AdminDeleteTeacher.html', exists='nothing')
    else:
        return render_template('AdminDeleteTeacher.html',exists='nothing')
    
@app.route("/AdminGiveTimeTable",methods=['POST','GET'] )
def AdminGiveTimeTable():
    if request.method=='POST':
        selectedClass=request.form.get("selectedClass")
        selectedDay=request.form.get("selectedDay")
        ttallotetime=request.form.get("ttallotetime")
        print(selectedClass)
        print(selectedDay)
        print(ttallotetime)
        return render_template("AdminGiveTimeTable.html")
    return render_template("AdminGiveTimeTable.html")

#Teacher Functions 
@app.route("/TeacherHomePage")
def TeacherHomePage():
    return render_template('TeacherHomePage.html',result=session.get('loginInfo'))

@app.route("/TeacherAttendancePage", methods=['POST','GET'])
def TeacherAttendancePage():
    if request.method=='GET':
        # selectedClass="CS"
        selectedClass = request.args.get('selectedClass')
        print(selectedClass)
        cursor.execute(f"SELECT studentID, {session.get('loginInfo')[5]} FROM ATTENDANCE WHERE CLASS=?", (selectedClass, ))
        result=cursor.fetchall()
        print(result)

        return render_template('TeacherAttendancePage.html')
    elif request.method=='POST':
        print('SUBMIT')
        return render_template('TeacherAttendancePage.html')
    else:
        return render_template('TeacherAttendancePage.html')

@app.route("/TeacherTimeTablePage")
def TeacherTimeTablePage():
    if request.method=='GET':
        day=request.args.get('DAYS')
        teacherID = session.get('loginInfo')[0]
        # print(teacherID)
        cursor.execute('select * from TIMETABLE where teacherID=? AND day=?', (teacherID, day,))
        result=cursor.fetchall()
        # print(procTimeTable(result, student=False))
        return render_template('TeacherTimeTablePage.html', ttable=procTimeTable(result, student=False))
    return render_template('TeacherTimeTablePage.html')
    
@app.route("/TeacherExamsPage", methods=['POST','GET'] )
def TeacherExamsPage():
    if request.method=='GET':   
        selectedClass = request.args.get('selectedClass')
        print(selectedClass)
        #apply sql query to get all students of that classes use for in html to loop all students
        return render_template('TeacherExamsPage.html')
    elif request.method=='POST':
        #once done selecting submit 
        print('SUBMIT')
        return render_template('TeacherExamsPage.html')
    else:
        return render_template('TeacherExamsPage.html')

#Student Functions
@app.route("/StudentHomePage")
def StudentHomePage():
    return render_template("StudentHomePage.html",result=session.get('loginInfo'))

@app.route("/StudentTimeTablePage")
def StudentTimeTablePage():
    if request.method=='GET':
        day=request.args.get('DAYS')
        cls = session.get('loginInfo')[13]
        print(cls)
        cursor.execute('select * from TIMETABLE where class=? AND day=?', (cls, day,))
        result=cursor.fetchall()
        # print(result)
        if result is not None:
            return render_template('StudentTimeTablePage.html',  ttable=procTimeTable(result))
    return render_template('StudentTimeTablePage.html')

@app.route("/StudentAttendancePage")
def StudentAttendancePage():
    cursor.execute('select * from ATTENDANCE where studentID=?', (session.get('loginInfo')[0],))
    result=cursor.fetchone()
    print(result)
    att = {}
    for index, data in enumerate(result):
        if index==1:
            att["DBMS"] = cvtData(data)
        elif index==2:
            att["IOT"] = cvtData(data)
        elif index==3:
            att["OOP"] = cvtData(data)
        elif index==4:
            att["DSA"] = cvtData(data)
        elif index==5:
            att["DS"] = cvtData(data)
        elif index==6:
            att["POPL"] = cvtData(data)
    return render_template("StudentAttendancePage.html", att=att)

def cvtData(data):
    lst = data.split("/")
    percent = (int(lst[0])/int(lst[1]))*100
    return round(percent, 2)

def procTimeTable(dataset, student=True):
    finalList = []
    for data in dataset:
        dct = {}
        if student:
            dct["sub"] = data[3]
        else:
            dct["class"] = data[2]
        lst = data[5].split("-")
        stime = ""
        etime = ""

        if int((lst[0].split(":"))[0]) > 12:
            stime = str(int((lst[0].split(":"))[0]) - 12)
            stime += ":"+ (lst[0].split(":"))[1]
            stime += " pm"
        else:
            stime = (lst[0].split(":"))[0]
            stime += ":"+ (lst[0].split(":"))[1]
            stime += " am"

        if int((lst[1].split(":"))[0]) > 12:
            etime = str(int((lst[1].split(":"))[0]) - 12)
            etime += ":"+ (lst[1].split(":"))[1]
            etime += " pm"
        else:
            etime = (lst[1].split(":"))[0]
            etime += ":"+ (lst[1].split(":"))[1]
            etime += " am"

        dct["start"] = stime
        dct["end"] = etime  
        finalList.append(dct)
    return finalList

@app.route("/StudentResultPage")
def StudentResultPage():
    return render_template("StudentResultPage.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
