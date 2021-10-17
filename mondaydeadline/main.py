from flask import Flask,jsonify,request,render_template,url_for,redirect,session
import secrets
import math

#https://flask.palletsprojects.com/en/2.0.x/quickstart/

app = Flask(__name__)

secret = secrets.token_urlsafe(32)

app.secret_key = secret


#login with validation
@app.route('/', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        if email=="joyston@gmail.com" and password=="joyston":
            session['msg'] = "Logged in Successfully"
            return redirect('/dashboard')
        else:
            msg = 'Incorrect username / password !'
    return render_template('Login.html', msg = msg)

@app.route('/dashboard')
def dashboard(msg=None):
    return render_template('Dashboard.html', msg=session['msg'])

@app.route('/add', methods =['GET', 'POST'])
def add():
    msg = ''
    result = ''
    if request.method == 'POST' and 'num7' in request.form and 'num8' in request.form:
        num7=int(request.form['num7'])
        num8=int(request.form['num8'])
        result=num7+num8
    return render_template('Add.html', msg = result)

@app.route('/subtract', methods =['GET', 'POST'])
def subtract():
    msg = ''
    result = ''
    if request.method == 'POST' and 'num9' in request.form and 'num10' in request.form:
        num9=int(request.form['num9'])
        num10=int(request.form['num10'])
        result=num9-num10
    return render_template('Subtract.html', msg = result)

@app.route('/multiply', methods =['GET', 'POST'])
def multiply():
    msg = ''
    result = ''
    if request.method == 'POST' and 'num1' in request.form and 'num2' in request.form:
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=num1*num2
    return render_template('Multiply.html', msg = result)

@app.route('/divide', methods =['GET', 'POST'])
def divide():
    msg = ''
    result = ''
    if request.method == 'POST' and 'num3' in request.form and 'num4' in request.form:
        num3=int(request.form['num3'])
        num4=int(request.form['num4'])
        result=num3/num4
    return render_template('Divide.html', msg = result)

@app.route('/armstrong', methods =['GET', 'POST'])
def armstrong():
    msg = ''
    result = ''
    if request.method == 'POST' and 'num5' in request.form:
        num5=request.form['num5']
        sum = 0
        order = len(str(num5))
        num = int(num5)    
        while(num>0):
            digit = num%10
            sum += digit **order
            num = num//10
        if(sum == int(num5)):
            result = f"{num5} is an armstrong number"
        else:
            result = f"{num5} is not an armstrong number"
    return render_template('Armstrong.html', msg = result)

@app.route('/factorial', methods =['GET', 'POST'])
def factorial():
    msg = ''
    result = ''
    if request.method == 'POST' and 'num6' in request.form:
        num6=request.form['num6']
        num = int(num6)    
        if(num >= 0):
            sum = math.factorial(num)
            result=f"The factorial of {num6} is {sum}"
        else:
            result="Invalid Input, Please Put a Positive Number"    
    return render_template('Factorial.html', msg = result)

@app.route('/evenorodd', methods =['GET', 'POST'])
def evenorodd():
    msg = ''
    result = ''
    if request.method == 'POST' and 'num11' in request.form:
        num11=int(request.form['num11'])
        if(num11%2==0):
            result="Even"
        else:
            result="Odd"
    return render_template('EvenorOdd.html', msg = result)

@app.route('/primeornot', methods =['GET', 'POST'])
def primeornot():
    msg = ''
    result = ''
    if request.method == 'POST' and 'num12' in request.form:
        num12=int(request.form['num12'])
        if(num12<0):
            result="Enter Valid Number"
        elif(num12==0 or num12==1):
            result="Neither Prime Nor Composite"    
        elif(num12==2):
            result="Prime"
        else:
            for i in range(2, num12):
                if (num12 % i) == 0:
                    result="Not Prime"
                    break
                else:
                    result="Prime"
    return render_template('PrimeorNot.html', msg = result)

"""
@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

def factorial():
    msg = ''
    result = ''
    if request.method == 'POST' and 'num6' in request.form:
        num6=request.form['num6']
        sum = 0
        num = int(num6)    
        while(num > 0):
            sum = (num)*(num-1)
            num = num-1

        if(num == 0):
            result = f"The factorial of {num6} is 1"
        elif(num < 0):
            result = "Invalid Input, please put a Positive Number"
        else:    
            result = f"The factorial of {num6} is {sum}"

    return render_template('Factorial.html', msg = result) 
"""

if __name__=="__main__":
    app.run(host="localhost",debug=True) 