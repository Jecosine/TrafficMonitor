from flask import Flask, request, jsonify
import json

app = Flask(__name__)
@app.route("/")
def fuck():
    return "banana"

@app.route("/receive", methods=['POST'])
def receiver():
    print dir(request)
    print "header",request.headers
    print "data", request.data
    print "form", request.form
    print "json", request.json
    return "fuck"

app.run(host="0.0.0.0", port=80, debug=True)