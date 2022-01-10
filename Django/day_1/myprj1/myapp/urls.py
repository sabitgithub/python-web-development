from django.urls import path
from myapp import views
urlpatterns = [
    path('v1/', views.myView1,name="sabit"),
    path('v2/<str:para1>/', views.myView2,name="sabit"),
    path('v3/<str:para1>/<str:para2>/', views.myView3,name="rabit"),
    path('index/', views.index,name="home"),
    path('about/', views.about,name="aboutme"),
]
