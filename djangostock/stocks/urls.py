from django.urls import path
from . import views

urlpatterns = [
    path('a', views.home, name='home'), # localhost:8000/a 접근 시, views.py에 가서 home 함수의 내용을 실행해라.
]
