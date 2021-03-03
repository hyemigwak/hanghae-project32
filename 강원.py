import pymongo



myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["dbsparta"]

mycol = mydb["travel_all"]

list = mycol.find({"location": "강원"})

for x in list:
    mydb.travel_gangwon.insert_one(x)