from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'Hello'
app.permanent_session_lifetime = timedelta(days=5)

@app.route('/user')
def user():
    if "user" in session:
        usr = session['user']
        return f"Hello My name is {usr}"
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print(request.form)
        user = request.form['nm']
        session['user'] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for('user'))
        return render_template('login.html')
    
@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)