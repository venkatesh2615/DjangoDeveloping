from django.urls import path,include
from app import views

urlpatterns = [
    path('', views.index,name='index'),
    path('index.html', views.index,name='index'),

    path('portfolio-details.html', views.index1,name='index1'),
    path('inner-page.html', views.index2,name='index2'),
    path('forms/contact.php', views.index2,name='s'),
]