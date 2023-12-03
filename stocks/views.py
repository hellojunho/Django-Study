from django.shortcuts import render
import requests
import json

def home(reqeust):
    try:
        ticker = reqeust.GET['ticker']
        stock_api = requests.get("https://api.iex.cloud/v1/data/core/quote/"+ticker+"?token=pk_0ebe670bfde7478984c98960631143b9")
        stock = json.loads(stock_api.content)   # url에서 get 해온 json 데이터를 dict 형태로 저장
    except Exception as e:
        stock = ""
        
    content = {'stock':stock}

    return render(reqeust, 'stocks/home.html', content)