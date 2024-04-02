import sqlite3 as sql
from flask import Flask, render_template, url_for, request, redirect                                        # From module flask import class Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#database configuration
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_insta')     #screen for user-id/pwd
def login_insta():
    return render_template('login_insta.html', title='Login')


@app.route('/check_login')     #screen for user-id/pwd
def login():
    print("DEBUG: Inside of authenticate")
    uname = request.args['username']
    pswd = request.args['password']
       
    # Do something with the form data
    print(f"UserId: {uname}")
    print(f"Password: {pswd}")
    
    #connect to database
    con = sql.connect(r"C:\Users\apauley24\Documents\GitHub\Instagram-Recreation-Project\instagram_database")
    con.row_factory = sql.Row

    #write query to see if user exists in the login table in the database
    cur = con.cursor()
    cur.execute("select user_id,username,password from user where username=" + "'" + uname + "'" + " and password=" + "'" + pswd + "'")
   
    rows = cur.fetchall(); 
    found = False
    
    for key,user_id,password in rows:
        found = True
        if found is True:                           #goto welcome screen
            print(found)
            return render_template("welcome.html", key=key, name=user_id)
    if found is False:
        return redirect(url_for('login_fail'))      #goto login_fail screen
    con.close()
    
    
    #return render_template('login_insta.html', title='Login')
    return

if __name__ == '__main__':
    app.run(debug=True)