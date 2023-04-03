from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('Checkin/', views.Checkin, name="Check In")

]