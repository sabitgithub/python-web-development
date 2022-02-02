from django.urls import path
from demoapp import views 

urlpatterns = [
    path('index/', views.index,name='home'),
    path('list/', views.list,name='list'),
    path('create/', views.create,name='create'),
    path('view/<int:id>', views.view_emp,name='view'),
    path('edit/<int:id>', views.edit,name='edit'),
]