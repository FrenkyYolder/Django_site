from django.urls import path
from polls import views

urlpatterns = [
    path('', views.main_page),
    path('second_page/', views.second_page)
]
