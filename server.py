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
    for i, tmp in enumerate(sample):
        del tmp["_id"]
        q_list.append(tmp)
    return(jsonify(q_list))

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/land', methods=['POST'])
def get_land():
    key = request.form['key']
    val = request.form['value']
    if key == 'ALL' or key == 'all':
        client = mongo_aba_init()
        db = client.abandonment
        coll = db.land
        all_land = coll.find()
        for tmp in all_land:
            del tmp["_id"]
            q_list.append(tmp)
        return(jsonify(q_list))

@app.route('/manage', methods=['POST'])
def get_manage():
    key = request.form['key']
    val = request.form['value']
    if key == 'ALL' or key == 'all':
        client = mongo_aba_init()
        db = client.abandonment
        coll = db.manage
        all_manage = coll.find()
        for tmp in all_manage:
            del tmp["_id"]
            q_list.append(tmp)
        return(jsonify(q_list))

@app.route('/user', methods=['POST'])
def get_user():
    key = request.form['key']
    val = request.form['value']
    if key == 'ALL' or key == 'all':
        client = mongo_aba_init()
        db = client.abandonment
        coll = db.land
        all_user = coll.find()
        for tmp in all_user:
            del tmp["_id"]
            q_list.append(tmp)
        return(jsonify(q_list))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
