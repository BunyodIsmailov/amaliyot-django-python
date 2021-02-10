from django.urls import path
from . import views

urlpatterns = [
    path('',views.body_funk,name="tana_qismi"),
    path('about/', views.about_funk, name="about_qismi"),
    path('home/', views.home_funk, name="home_qismi"),
    path('settings/', views.yurak_funk, name="settings_qismi")
]