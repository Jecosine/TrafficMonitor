from flask import Flask, request, jsonify, make_response
import json
import random



d = {'data':[]}
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
@app.route("/delive", methods=['GET'])
def deliver():
    global d
    if len(d['data']) > 20:
        d['data'].pop(0)
    d['data'].append(random.randint(0,200))
    r = make_response(json.dumps(d), 201)
    r.headers["Access-Control-Allow-Origin"]="*"
    r.headers['content-type']="application/json"
    # r.headers["Access-Control-Allow-Credentials"]="true"
    # r.headers['Access-Control-Allow-Methods'] = 'POST'
    # r.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
   
    return r
app.run(host="0.0.0.0", port=80, debug=True)