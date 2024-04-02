

from flask import Flask  # From module flask import class Flask
from flask import render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql

app = Flask(__name__)    # Construct an instance of Flask class for our webapp

#database configuration
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

@app.route('/')   # URL '/' to be handled by main() route handler



@app.route('/login_insta')       #screen for user-id/pwd
def login_insta():
    return render_template('login_insta.html', title='Login')



    
@app.route('/authenticate')
def authenticate():
    #get user_id && pwd to connect to db
    print("DEBUG: Inside of authenticate")
   
    if request.method == "GET":
        print("31")
        # Get the form data
        
        uname = request.args['uname']
        pswd = request.args['pswd']
       
        # Do something with the form data
        print(f"UserId: {uname}")
        print(f"Password: {pswd}")
        
    con = sql.connect(r"C:\Users\apauley24\Documents\GitHub\Instagram-Recreation-Project\instagram_database")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select id,username,password from login where username=" + "'" + uname + "'" + " and password=" + "'" + pswd + "'")
   
    rows = cur.fetchall(); 
    found = False
    
    for key,user_id,password in rows:
        found = True
        if found is True:                           #goto welcome screen
            print(found)
            return render_template("welcome.html", key=key)
    if found is False:
        return redirect(url_for('login_fail'))      #goto login_fail screen
    #con.close()

@app.route('/login_fail')
def login_fail():
    return render_template("login_fail.html")

@app.route('/index')
def index():
   
    #return render_template('index.html', title='Welcome')
    return render_template('login_insta.html', title='Welcome')
   

if __name__ == '__main__':  # Script executed directly?
    
    app.debug = True
    app.run()  # Launch built-in web server and run this Flask webapp