from flask import *
from pymongo import MongoClient
import json

app = Flask(__name__)

def mongo_aba_init():
    host = 'localhost'
    port = 27017
    db = 'abandonment'
    user = 'online_user'
    pwd = 'servicetech'
    client = MongoClient(host, port)
    return client

def mongo_acc_init():
    host = 'localhost'
    port = 27017
    db = 'account'
    user = 'online_user'
    pwd = 'servicetech'
    client = MongoClient(host, port)
    return client

@app.route('/')
def index():
    client = mongo_aba_init()
    db = client.abandonment
    coll = db.land
    sample = coll.find()
    q_list = []
    for tmp in sample:
        tmp["_id"] = str(tmp["_id"])
        q_list.append(tmp)
    return(jsonify(q_list))

@app.route('/land', methods=['POST','GET'])
def get_land():
    if request.method == "GET":
        key = request.args.get("key","")
    elif request.method == "POST":
        key = request.form['key']
    if key == 'ALL' or key == 'all':
        client = mongo_aba_init()
        db = client.abandonment
        coll = db.land
        all_land = coll.find()
        q_list = []
        for tmp in all_land:
            tmp["_id"] = str(tmp["_id"])
            q_list.append(tmp)
        return(jsonify(q_list))

@app.route('/manage', methods=['POST','GET'])
def get_manage():
    if request.method == "GET":
        key = request.args.get("key","")
    elif request.method == "POST":
        key = request.form['key']
    if key == 'ALL' or key == 'all':
        client = mongo_aba_init()
        db = client.abandonment
        coll = db.manage
        all_manage = coll.find()
        q_list = []
        for tmp in all_manage:
            tmp["_id"] = str(tmp["_id"])
            q_list.append(tmp)
        return(jsonify(q_list))

@app.route('/user', methods=['POST','GET'])
def get_user():
    if request.method == "GET":
        key = request.args.get("key","")
    elif request.method == "POST":
        key = request.form['key']
    if key == 'ALL' or key == 'all':
        client = mongo_aba_init()
        db = client.abandonment
        coll = db.land
        all_user = coll.find()
        q_list = []
        for tmp in all_user:
            tmp["_id"] = str(tmp["_id"])
            q_list.append(tmp)
        return(jsonify(q_list))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
