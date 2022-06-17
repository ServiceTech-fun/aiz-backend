from flask import *
from pymongo import MongoClient
from bson.objectid import ObjectId
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
    return render_template('index.html')

@app.route('/land', methods=['POST','GET'])
def get_land():
    if request.method == "GET":
        key = request.args.get("key","")
        val = request.args.get("val","")
    elif request.method == "POST":
        key = request.form['key']
        val = request.form['val']
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
    else:
        client = mongo_aba_init()
        db = client.abandonment
        coll = db.land
        if key == '_id':
            search_tgt = {key : ObjectId(val)}
            search_land = coll.find_one(search_tgt)
            search_land["_id"] = str(search_land["_id"])
            return(jsonify(search_land))
        else:
            search_tgt = {key : val}
            search_land = coll.find(search_tgt)
            q_list = []
            for tmp in search_land:
                tmp["_id"] = str(tmp["_id"])
                q_list.append(tmp)
            return(jsonify(q_list))


@app.route('/manage', methods=['POST','GET'])
def get_manage():
    if request.method == "GET":
        key = request.args.get("key","")
        val = request.args.get("val","")
    elif request.method == "POST":
        key = request.form['key']
        val = request.form['val']
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
    else:
        client = mongo_aba_init()
        db = client.abandonment
        coll = db.manage
        if key == '_id':
            search_tgt = {key : ObjectId(val)}
            search_resv = coll.find_one(search_tgt)
            search_resv["_id"] = str(search_resv["_id"])
            return(jsonify(search_resv))
        else:
            search_tgt = {key : val}
            search_resv = coll.find(search_tgt)
            q_list = []
            for tmp in search_resv:
                tmp["_id"] = str(tmp["_id"])
                q_list.append(tmp)
            return(jsonify(q_list))

@app.route('/user', methods=['POST','GET'])
def get_user():
    if request.method == "GET":
        key = request.args.get("key","")
        val = request.args.get("val","")
        state = request.args.get("state","")
    elif request.method == "POST":
        key = request.form['key']
        val = request.form['val']
        state = request.form['state']
    if key == 'ALL' or key == 'all':
        client = mongo_acc_init()
        db = client.account
        coll = db.user
        all_user = coll.find()
        q_list = []
        for tmp in all_user:
            tmp["_id"] = str(tmp["_id"])
            q_list.append(tmp)
        return(jsonify(q_list))
    else:
        if state == 'get':
            client = mongo_acc_init()
            db = client.account
            coll = db.user
            if key == '_id':
                search_tgt = {key : ObjectId(val)}
                search_user = coll.find_one(search_tgt)
                search_user["_id"] = str(search_user["_id"])
                return(jsonify(search_user))
            elif key == "email" or key == "tel":
                search_tgt = {key : val}
                search_user = coll.find_one(search_tgt)
                search_user["_id"] = str(search_user["_id"])
                return(jsonify(search_user))
            else:
                search_tgt = {key : val}
                search_user = coll.find(search_tgt)
                q_list = []
                for tmp in search_user:
                    tmp["_id"] = str(tmp["_id"])
                    q_list.append(tmp)
                return(jsonify(q_list))
        elif state == 'create':
            myclient = MongoClient("mongodb://localhost:27017/")
            mydb = myclient["account"]
            mycol = mydb["user"]
            if request.method == "GET":
                passwd = request.args.get("passwd","")
                age = request.args.get("age","")
                category = request.args.get("category","")
                email = request.args.get("email","")
                family = request.args.get("family","")
                first = request.args.get("first","")
                sex = request.args.get("sex","")
                tel = request.args.get("tel","")
                tools = request.args.get("tools","")
            elif request.method == "POST":
                passwd = request.form['passwd']
                age = request.form['age']
                category = request.form['category']
                email = request.form['email']
                family = request.form['family']
                first = request.form['first']
                sex = request.form['sex']
                tel = request.form['tel']
                tools = request.form['tools']
            res = mycol.insert_one({"passwd":passwd,"age":age,"category":category,"email":email,"family":family,"first":first,"sex":sex,"tel":tel,"tools":tools})
            return(jsonify(str(res)))



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
