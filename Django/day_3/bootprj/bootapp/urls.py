from django.urls import path
from bootapp import views

urlpatterns = [
    path('index/', views.index,name='home'),
    path('list/', views.list,name='list'),
]
