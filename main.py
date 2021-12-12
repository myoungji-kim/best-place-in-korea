import crawling, mapping
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def drawing_map():
        # 데이터 수집 대상
        url = 'https://www.google.com/travel/things-to-do?g2lb=4597339%2C4667459%2C4644488%2C4596364%2C4605861%2C4419364%2C4641139%2C2502548%2C2503781%2C4624411%2C4518326%2C2503771%2C4401769%2C4306835%2C4640247%2C4258168%2C4371335%2C4317915%2C4270442%2C4679298%2C4284970%2C4291517%2C4270859&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F06qd3&dest_state_type=main&dest_src=ts&q=%ED%95%9C%EA%B5%AD%20%EA%B4%80%EA%B4%91%20%EB%AA%85%EC%86%8C%20top%2010&sa=X&ved=2ahUKEwiK9Pm1hdn0AhXcr1YBHTKMBBMQuL0BegQIAxA-#ttdm=37.523965_127.473897_8&ttdmf=%252Fm%252F043pdws'
        
        # 장소 리스트를 변수에 저장
        titles = crawling.crawling_sites(url)[0]
        scores = crawling.crawling_sites(url)[1]
        cnt_reviews = crawling.crawling_sites(url)[2]
        infos = crawling.crawling_sites(url)[3]
        images = crawling.crawling_sites(url)[4]
        

        # 시각화 결과물 템플릿을 html_map 변수에 담기 (단, 시각화 결과물객체 뒤에  ._repr_html_() 붙이기)
        html_map = mapping.drawing_map(url)._repr_html_()  # _repr_html_ : html화 하는 함수

        # render_template() 내부 파라미터 작성하기
        return render_template("index.html", map = html_map, 
                               title = titles, score = scores, cnt_review = cnt_reviews, info = infos, image = images)

if __name__ == "__main__":
	app.run(host = "127.0.0.1", port = 5000, debug = True)