import pymongo



myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["dbsparta"]

mycol = mydb["travel_final"]

list = mycol.find({"location": "서울"})

for x in list:
    mydb.travel_seoul.insert_one(x)