from django.urls import path
from demoapp import views 

urlpatterns = [
    path('index/', views.index,name='home'),
]