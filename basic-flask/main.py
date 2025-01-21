from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base_index.html')
    # return render_template('index.html')
    # return "Hello! this is the main page <h1> HELLO </h1>"

@app.route('/<name>')
def user(name):
    return f"Hello {name}"

@app.route('/admin')
def admin():
    return redirect(url_for('home'))

@app.route('/admin1/')
def admin1():
    return redirect(url_for('user', name='ADMIN1'))

@app.route('/users')
def userlist():
    user_list = ['Sanjay', 'Vijay', 'Mahesh', 'Ashok']
    return render_template('users.html',name='Rahul', user_list=user_list)


if __name__ == '__main__':
    app.run(debug=True)