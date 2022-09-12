import flask as fl 

app = fl.Flask(__name__)

@app.route("/")
def say_hello():
    return "Hi Mom!"
    

