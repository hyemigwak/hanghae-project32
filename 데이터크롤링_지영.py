import requests
from bs4 import BeautifulSoup

#DB코드
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C2503806%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371335%2C4401769%2C4419364%2C4429192%2C4463666%2C4482194%2C4482438%2C4486153%2C4491350%2C4495816%2C4504283%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&dest_mid=%2Fm%2F06qd3&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjZgN_v0Y7vAhXI62EKHUDACGYQuL0BMAN6BAgQEDg#ttdm=37.433657_127.251424_9&ttdmf=%252Fm%252F07zj3q',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

divs = soup.select('#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div.lteUWc > div > c-wiz > div > div > div.zpbwad.mNY2uf > div:nth-child(3) > c-wiz > div > div > div > div > div')
for div in divs:
    name_tag = div.select_one('div > div > div.Ld2paf > div.GwjAi > div.rbj0Ud').text
    img_tag = div.select_one('div > div > div.Ld2paf > div.kXlUEb').img
    img_src = img_tag.get("data-src")  # 이미지 경로
    description = div.select_one('div > div > div.Ld2paf > div.GwjAi > div.nFoFM').text

    doc = {
        'place':name_tag,
        'img_url':img_src,
        'description': description
    }
    db.travel_final.insert_one(doc)
