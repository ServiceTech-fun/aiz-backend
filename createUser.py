import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["account"]
mycol = mydb["user"]

x = mycol.insert_one({"passwd":"g2121030","age":23.0,"category":"administrator","email":"g21210300d@edu.teu.ac.jp","family":"Takagi","first":"Yuuki","sex":"man","tel":"09066181424","tools":""})
x = mycol.insert_one({"passwd":"g2121031","age":23.0,"category":"administrator","email":"g21210317b@edu.teu.ac.jp","family":"Takaya","first":"Yutaro","sex":"man","tel":"","tools":""})
x = mycol.insert_one({"passwd":"ojioji","age":55.0,"category":"owner","email":"xxxb@gmail.com","family":"Oji","first":"Oji","sex":"man","tel":"","tools":"weapon"})