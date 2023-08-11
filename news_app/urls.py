from django.urls import path
from .views import News_list,News_detail,homeView,contactPageView,error404,HomePageView,localNews,texnoPage,sportPage,xorijPage



urlpatterns = [
    path('',HomePageView.as_view(),name='home_page'),
    path('news/',News_list,name="news_list_page"),
    path('news/<slug:news>',News_detail,name="news_detail_page"),
    path('contact-us/',contactPageView.as_view(),name="contact-page"),
    path('404/',error404,name='404_page'),
    path('local/',localNews.as_view(),name="local_page"),
    path('xorij/',xorijPage.as_view(),name="xorij_page"),
    path('sport/',sportPage.as_view(),name="sport_page"),
    path('texnologiya/',texnoPage.as_view(),name="texno_page")
]