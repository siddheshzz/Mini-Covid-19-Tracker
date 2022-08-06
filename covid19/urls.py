from django.urls import path,include
from covid19 import views

urlpatterns = [
    path('',views.index),
    path('map/', views.index1)
]
