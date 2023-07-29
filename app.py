from flask import Flask,request,render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def  welcome():
    return "welcome to Flask"

@app.route('/cal', methods = ["GET"])
def math_operations():
    operation = request.json["operation"]
    num1 =  request.json["num1"]
    num2 =  request.json["num2"]

    if operation == "add":
        result = int(num1) + int(num2)
    elif operation == "multiply":
        result = int(num1)*int(num2)  
    elif operation == "division":
        result = int(num1)/int(num2)
    else :
        result = int(num1)-int(num2)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug = True)