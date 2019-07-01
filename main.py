from flask import Flask, request,render_template,redirect
import re
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup", methods=['GET','POST'])
def username_validation():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']   
        v_password = request.form['vpassword']
        email = request.form['email']
        invalid = False
        username_error = None
        password_error = None
        vpassword_error = None
        email_error = None

        valid = re.compile(r"(^[0-9a-zA-Z_]{3,20}$)")

        if not valid.match(username):
            username_error = "That's not valid Username" 
            invalid = True
        if not valid.match(password):
            password_error = "That's not valid Password"
            invalid = True
        if  v_password == '' or v_password != password:
            vpassword_error = "Passwords don't match"
            invalid = True
        if email.strip() != '' and not re.match(r"(^[0-9a-zA-Z_]+@[0-9a-zA-Z]+\.[a-zA-Z]+$)", email):
            email_error = "Invalid email"  
            invalid = True

        if invalid:    
            return render_template('user-form.html', username=username, email=email, username_error=username_error, password_error=password_error, vpassword_error=vpassword_error, email_error=email_error)
        else:
            return render_template('welcome.html', username=username)
    else:
        return render_template('user-form.html') 


@app.route("/")
def index():
    return redirect('/signup')  

app.run()