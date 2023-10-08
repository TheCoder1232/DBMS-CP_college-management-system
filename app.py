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
                 return render_template("Profile.html")
            elif result[2]=='T':
                return render_template("login_page.html")
            elif result[2]=='S':
                return render_template("login_page.html")
        else:
            return render_template("login_page.html", exist=False)
    else:
        return render_template("login_page.html", exist=True)
    
@app.route("/StudentAttendance")
def StudentAttendance():
    return render_template("StudentAttendance.html")

@app.route("/Profile")
def Profile():
    return render_template("Profile.html")


# @app.route("/update/<int:sno>", methods=['GET', 'POST'])
# def update(sno):
#     if request.method=="POST":
#         title = request.form["title"]
#         desc = request.form["desc"]
#         todo = Todo.query.filter_by(sno=sno).first()
#         todo.title = title
#         todo.desc = desc
#         db.session.add(todo)
#         db.session.commit()
#         return redirect("/")
    
#     todo = Todo.query.filter_by(sno=sno).first()
#     return render_template("update.html", todo=todo)

# @app.route("/delete/<int:sno>")
# def delete(sno):
#     todo = Todo.query.filter_by(sno=sno).first()
#     db.session.delete(todo)
#     db.session.commit()
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
