import requests
from bs4 import BeautifulSoup

# 리스트에 데이터 추가하는 함수
def add_list(group, list):
    for one in group:
        list.append(one.get_text())


def crawling_sites(url):
    response = requests.request('GET', url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 데이터 수집 위치 + 저장할 리스트 생성
    titles = soup.select('div.rbj0Ud div')
    places_title = []

    scores = soup.select('div.tP34jb span.KFi5wf.lA0BZ')
    places_score = []

    cnt_reviews = soup.select('div.tP34jb span.jdzyld.XLC8M')
    places_cnt_review = []

    infos = soup.select('div.nFoFM')
    places_info = []
    
    images = soup.select('img.R1Ybne.YH2pd')
    places_image = []
    
    for one in images[1:]:
        places_image.append(one['data-src'])

    add_list(titles, places_title)
    add_list(scores, places_score)
    add_list(cnt_reviews, places_cnt_review)
    add_list(infos, places_info)

    return places_title, places_score, places_cnt_review, places_info, places_image