import pymongo



myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["dbsparta"]

mycol = mydb["travel_final"]

list = mycol.find({"location": "경기"})

for x in list:
    mydb.travel_gyeong_gi.insert_one(x)