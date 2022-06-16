import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["abandonment"]
mycol = mydb["land"]

x = mycol.insert_one({ "userid" : "62a9e1aba133eae73b57ff96", "name" : "OjiOjiland2", "waive" : 5, "vertical" : 200, "horizontal" : 100, "comment" : "test", "image" : "https://agrijobwp.s3.ap-northeast-1.amazonaws.com/2022/05/01181200/3bc663b537abc8774d93123e2371542b-1-scaled.jpeg", "state" : "Available", "usage": "Agriculture" })
x = mycol.insert_one({ "userid" : "62a9e1aba133eae73b57ff96", "name" : "OjiOjiland3", "waive" : 8, "vertical" : 100, "horizontal" : 150, "comment" : "douzo~", "image" : "https://agrijobwp.s3.ap-northeast-1.amazonaws.com/2022/05/11110100/tbi2.jpg", "state" : "Wanted", "usage": "Agriculture" })
x = mycol.insert_one({ "userid" : "62a9e1aba133eae73b57ff96", "name" : "OjiOjiland4", "waive" : 10, "vertical" : 80, "horizontal" : 80, "comment" : "douzo!", "image" : "https://agrijobwp.s3.ap-northeast-1.amazonaws.com/2022/05/11110347/tbi3.jpg", "state" : "Wanted", "usage": "Agriculture"})
x = mycol.insert_one({ "userid" : "62a9e1aba133eae73b57ff96", "name" : "OjiOjiland5", "waive" : 1, "vertical" : 50, "horizontal" : 50, "comment" : "sorry", "image" : "https://agrijobwp.s3.ap-northeast-1.amazonaws.com/2022/05/11110644/tbi4.jpg", "state" : "Ended", "usage": "Agriculture" })
x = mycol.insert_one({ "userid" : "62a9e1aba133eae73b57ff96", "name" : "OjiOjiland", "waive" : 10, "vertical" : 100, "horizontal" : 100, "comment" : "douzo~", "image" : "https://upload.wikimedia.org/wikipedia/commons/7/70/Abandoned_Paddy_Field_in_Japan.jpg", "state" : "Wanted", "usage": "Agriculture" })