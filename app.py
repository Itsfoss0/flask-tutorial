import flask as fl 


dotenv.load_dotenv()
app = fl.Flask(__name__)

@app.route("/")
def say_hello():
    return "Hi Mom!"
    

