from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)
conn = sqlite3.connect('./instance/ERP-.db', check_same_thread=False)
cursor = conn.cursor()
app.app_context().push()

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
    

    
@app.route("/StudentAttendancePage")
def StudentAttendancePage():
    return render_template("StudentAttendancePage.html")

@app.route("/StudentHomePage")
def StudentHomePage():
    return render_template("StudentHomePage.html")


#Admin Functions
@app.route("/AdminHomePage")
def AdminHomePage():
    return render_template("AdminHomePage.html")


@app.route("/AdminAddStudent")
def AdminAddStudent():
    return render_template('AdminAddStudent.html')

@app.route("/AdminDeleteStudent")
def AdminDeleteStudent():
    return render_template('AdminDeleteStudent.html')


@app.route("/AdminAddTeacher")
def AdminAddTeacher():
    return render_template('AdminAddTeacher.html')

@app.route("/AdminDeleteTeacher")
def AdminDeleteTeacher():
    return render_template('AdminDeleteTeacher.html')





if __name__ == "__main__":
    app.run(debug=True, port=8000)
