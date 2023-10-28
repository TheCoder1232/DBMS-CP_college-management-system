from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)
conn = sqlite3.connect('./instance/ERP-.db', check_same_thread=False)
cursor = conn.cursor()
app.app_context().push()

#Login Function
@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method=="POST":
        email = request.form["login_email"]
        password = request.form["login_password"]
        cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        result = cursor.fetchone()
        if result is not None:
            if result[2]=='A':
                 return render_template("AdminHomePage.html")
            elif result[2]=='T':
                return render_template("TeacherHomePage.html")
            elif result[2]=='S':
                return render_template("StudentHomePage.html")
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

       
        return render_template('AdminAddStudent.html' ,success=True)
    else:
        return render_template('AdminAddStudent.html')

@app.route("/AdminDeleteStudent" ,methods=['POST','GET'])
def AdminDeleteStudent():
    if request.method=="POST":
        uid=request.form["UID1"]
        print(uid)
        if uid=='1':
            return render_template('AdminDeleteStudent.html', exists=True)
        else:
            return render_template('AdminDeleteStudent.html', exists=False)
    elif request.method=='GET':
        return render_template('AdminDeleteStudent.html', exists='nothing')
    else:
        return render_template('AdminDeleteStudent.html',exists='nothing')
        

       

@app.route("/AdminAddTeacher", methods=['POST','GET'])
def AdminAddTeacher():
    if request.method=="POST":
        TeacherNamee=request.form["TeacherName"]
        PNo=request.form["PNo"]
        Addr=request.form["Addr"]
        UID=request.form["UID"]
        EXP=request.form["EXP"]
        DOB=request.form["DOB"]
        SUBJ=request.form["SUBJ"]
        Email=request.form["Email"]
        Password=request.form["Password"]
        print('done')
        return render_template('AdminAddTeacher.html' ,success=True)
    else:
        return render_template('AdminAddTeacher.html')

@app.route("/AdminDeleteTeacher" ,methods=['POST','GET'])
def AdminDeleteTeacher():
    if request.method=="POST":
        uid=request.form["UID1"]
        print(uid)
        if uid=='1':
            
            return render_template('AdminDeleteTeacher.html', exists=True)
        else:
            return render_template('AdminDeleteTeacher.html', exists=False)
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
