from flask import Flask,jsonify,request,render_template,url_for,redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors
import yaml
import re

#https://flask.palletsprojects.com/en/2.0.x/quickstart/

app = Flask(__name__)

# Configure db
db = yaml.full_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = int(n)    
    while(n>0):
        digit = n%10
        sum += digit **order
        n = n//10

    if(sum == copy_n):
        return f"{copy_n} is an armstrong number"
    else:
        return f"{copy_n} is not an armstrong number"


@app.route('/in_out',methods=['POST','GET'])
def inout():
    if request.method == 'POST':
        inout=request.form['input']
        return redirect(url_for('armstrong', n=inout))
    return render_template('in_out.html')
    
"""       
#testing
@app.route('/reg', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)
"""

# login register implement
# register with validation
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'fname' in request.form and 'lname' in request.form and 'dob' in request.form and 'email' in request.form and 'password' in request.form:
        # Fetch form data
        fname = request.form['fname']
        lname = request.form['lname']
        dob = request.form['dob']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT * FROM logreg WHERE email = % s', (email, ))
        registered = cur.fetchone()
        if registered:
            msg = 'Account already exists !'
        elif not fname or not lname or not dob or not email or not password:
            msg = 'Please fill out the form !'

        elif not re.match(r'[A-Za-z0-9]+', fname):
            msg = 'First name must contain only characters and numbers !'
        elif not re.match(r'[A-Za-z0-9]+', lname):
            msg = 'Last name must contain only characters and numbers !'    
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'           
        else:
            cur.execute("INSERT INTO logreg(fname, lname, dob, email, password) VALUES(%s, %s, %s, %s, %s)",(fname, lname, dob, email, password))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
            mysql.connection.commit()
            cur.close()
            return redirect('/login')
    elif request.method == 'POST':
        msg = 'Please fill out the form !'        
    return render_template('Register.html', msg = msg)

#login with validation
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM logreg WHERE email = % s && password = % s', (email, password, ))
        existing_user = cursor.fetchone()
        if existing_user:
            msg = 'Logged in successfully !'
            return render_template('in_out.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('Login.html', msg = msg)

if __name__=="__main__":
    app.run(host="localhost",debug=True) 