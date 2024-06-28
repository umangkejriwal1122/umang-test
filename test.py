from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    return "Hello World"

app.run(host='0.0.0.0')