from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('base/', views.base,name='base'),
    path('', views.home,name='Home'),
    path('<int:id>/', views.index,name='int work'),
    path('v1/', views.v1,name='v1'),
    path('create/', views.create,name='create'),
    path('success/', views.success,name='success')



  

]
