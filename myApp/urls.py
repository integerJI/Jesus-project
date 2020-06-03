from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('save/', views.save, name="save"),
    path('calender/', views.calender, name="calender"),
    path('dev/', views.dev, name="dev"),
]
