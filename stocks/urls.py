from django.urls import path
from . import views

urlpatterns = [
    # path('a', views.home, name='home'),
    path('a', views.home, name='home'),
    path('', views.main, name='main')
]
 