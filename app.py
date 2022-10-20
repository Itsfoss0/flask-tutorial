from flask import Flask, render_template, flash
import requests 
app = Flask(__name__)

@app.route("/index",methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/greetings", methods=['GET', 'POST'])
def greet():
    render_template("index.html", message=requests.form.get("message"))  
if __name__ == "__main__":
    app.run(debug=False)
