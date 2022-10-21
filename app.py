from flask import Flask, url_for, redirect 
import requests 


app = Flask(__name__)

@app.route("/index/admin")
def admin_rule():
    return "<h1 align='center'> Hi There Admin!!!</h1>"

@app.route("/index/guest")
def guest_user():
    return "<h2> Nice to see you Guest </h2>"


@app.route('/index/<role>')
def index(role):
    if (role.strip().lower() == "admin"):
        return redirect(url_for('admin_rule'))
    elif (role.strip().lower() == "guest"):
        return redirect(url_for('guest_user'))
    else:
        return "<h3> Great !! </h3>"

if __name__ == "__main__":
    app.run(debug=False)
