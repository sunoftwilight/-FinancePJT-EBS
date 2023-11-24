from django.shortcuts import render
import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
import datetime


# API 요청
@api_view(['GET'])
def getchange(request):
    API_KEY = '5VkPZBZNY6SWF4HnGla0BMlUn1fu9X9J'
    
    
    # 오늘의 요일 정수형으로 가져오기
    print(datetime.datetime.today().weekday())

    # (11시 이전에는 Null값 들어오므로) 영업일 11시 이후 데이터만 가져오기 
    now_date = datetime.datetime.today() # strftime('%Y%m%d')
    year = int(now_date.strftime('%Y'))
    month = int(now_date.strftime('%m'))
    day = int(now_date.strftime('%d'))
    time = int(now_date.strftime('%H'))
    if now_date.weekday() == 5:
        day -= 1 
    elif now_date.weekday() == 6:
        day -= 2

    elif time < 11:
        day -= 1

    date = datetime.date(year, month, day)
    
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&searchdate={date}&data=AP01'
    print('https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=5VkPZBZNY6SWF4HnGla0BMlUn1fu9X9J&data=AP01')
    response = requests.get(url)    
    response=response.json()


    return JsonResponse(response, safe=False)