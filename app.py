from flask import Flask, url_for, redirect, render_template
import requests 


app = Flask(__name__)

@app.route("/index/admin")
def admin_rule():
    return "<h1 align='center'> Hi There Admin!!!</h1>"

@app.route("/index/guest")
def guest_user():
    return "<h2> Nice to see you Guest </h2>"

"""
@app.route('hello', methods=["GET", "POST"])
def say_hello(user):
    return render_template('index.html', name=user)
"""

@app.route('/index/<role>')
def index(role):
    if (role.strip().lower() == "admin"):
        return redirect(url_for('admin_rule'))
    elif (role.strip().lower() == "guest"):
        return redirect(url_for('guest_user'))
    else:
        return redirect(url_for('say_hello', name=user))

@app.route('/todo')
def todo():
    todo_list = ['Wash Utensils', 'Learn Flask', 'Learn Kubernetes', 'Learn Docker']
    return render_template('index.html', todo_list=todo_list)

if __name__ == "__main__":
    app.run(debug=False)
