from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('main.html')

@app.route('/mypage')
def mypage():
    return render_template('mypage.html')

    ## 각 지역별 페이지 불러옴
@app.route('/서울')
def 서울():
    return render_template('서울.html')
@app.route('/경기')
def 경기():
    return render_template('경기.html')
@app.route('/부산')
def 부산():
    return render_template('부산.html')
@app.route('/제주')
def 제주():
    return render_template('제주.html')
@app.route('/경주')
def 경주():
    return render_template('경주.html')
@app.route('/강원')
def 강원():
    return render_template('강원.html')


# API 역할을 하는 부분

@app.route('/api/list', methods=['GET'])
def show_stars():
    travel = list(db.travel_all.find({},{'_id':False}))
    return jsonify({'travel': travel})

@app.route('/api/delete', methods=['POST'])
def delete_star():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'delete 연결되었습니다!'})

@app.route('/api/like', methods=['POST'])
def like_star():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'like 연결되었습니다!'})


# API 각 지역별 리스트 불러옴
@app.route('/api/서울', methods=['GET'])
def click_seoul():
    travel_seoul = list(db.travel_seoul.find({},{'_id':False}))
    return jsonify({'travel_seoul': travel_seoul})

@app.route('/api/경기', methods=['GET'])
def click_gyeong_gi():
    travel_gyeong_gi = list(db.travel_gyeong_gi.find({},{'_id':False}))
    return jsonify({'travel_gyeong_gi': travel_gyeong_gi})

@app.route('/api/부산', methods=['GET'])
def click_busan():
    travel_busan = list(db.travel_busan.find({},{'_id':False}))
    return jsonify({'travel_busan': travel_busan})


@app.route('/api/제주', methods=['GET'])
def click_jeju():
    travel_jeju = list(db.travel_jeju.find({},{'_id':False}))
    return jsonify({'travel_jeju': travel_jeju})

@app.route('/api/경주', methods=['GET'])
def click_gyeongju():
    travel_gyeongju = list(db.travel_gyeongju.find({},{'_id':False}))
    return jsonify({'travel_gyeongju': travel_gyeongju})

@app.route('/api/강원', methods=['GET'])
def click_gangwon():
    travel_gangwon = list(db.travel_gangwon.find({},{'_id':False}))
    return jsonify({'travel_gangwon': travel_gangwon})


if __name__ == '__main__':
        app.run('0.0.0.0', port=5000, debug=True)