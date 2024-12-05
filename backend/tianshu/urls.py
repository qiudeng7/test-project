from django.urls import path
from . import views

# 当访问playground/hello的时候，把请求交给views.hello处理
urlpatterns= [
    path('hello/',views.hello)
]