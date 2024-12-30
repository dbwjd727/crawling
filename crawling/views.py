# views.py
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import logging

# logging.getLogger('django')를 사용하여 Django 로깅 설정을 따릅니다.
logger = logging.getLogger("django")


def get_stock_data(request):
    # 크롤링할 주식 URL 설정 (예: 삼성전자 주식)
    stock_code = "005930"  # 삼성전자
    url = f"https://finance.naver.com/"

    logger.info(f"요청 보낼 url: {url}")

    # 웹 페이지 요청
    response = requests.get(url)

    # 응답 상태 코드 확인
    if response.status_code != 200:
        return HttpResponse(f"크롤링 실패! 상태 코드: {response.status_code}")

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    # logger.info(f"soup???????: {soup}")

    # 여러 행을 반복문으로 크롤링
    stock_info = ""  # 결과를 저장할 변수

    # 페이지가 제대로 로드되었는지 확인
    try:
        for i in range(1, 10):  # tr:nth-child(1)부터 tr:nth-child(4)까지
            # 각 열에서 필요한 데이터 추출
            name = soup.select_one(f"#_topItems1 > tr:nth-child({i}) > th > a")
            price = soup.select_one(
                f"#_topItems1 > tr:nth-child({i}) > td:nth-child(2)"
            )
            update = soup.select_one(
                f"#_topItems1 > tr:nth-child({i}) > td:nth-child(3)"
            )
            upercent = soup.select_one(
                f"#_topItems1 > tr:nth-child({i}) > td:nth-child(4)"
            )

            # 데이터가 있는 경우만 출력
            if name and price and update and upercent:
                stock_info += f"주식 이름: {name.text.strip()}<br>"
                stock_info += f"주식 가격: {price.text.strip()}<br>"
                stock_info += f"변화: {update.text.strip()}<br>"
                stock_info += f"변동률: {upercent.text.strip()}<br><br>"

        # 결과를 HTTP 응답으로 반환
        return HttpResponse(stock_info)

    except AttributeError:
        return HttpResponse("주식 정보를 추출하는 데 실패했습니다.")
