from django.urls import path 
from codeplay_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('kids/', views.kids, name='kids'),  
    path('teen/', views.teen, name='teen'),  
    path('about/', views.about, name='about'),
    path('pendaftaran/', views.pendaftaran, name='pendaftaran'),
    path('signin/', views.signin, name='signin'),
]
