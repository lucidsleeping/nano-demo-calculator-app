from flask import Flask,request, jsonify
# from dataclasses import dataclass

# @dataclass
# class Convert : 
#     result : int 

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json 
    res = int(data['first'] + data['second'])
    return jsonify(res)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json 
    res = int(data['first'] - data['second'])
    return jsonify(res) 

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')