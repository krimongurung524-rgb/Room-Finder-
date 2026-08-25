from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('create/', views.room_create, name='room_create'),
    path('my-page/', views.my_static_page, name='my_static_page'),
    path('<slug:slug>/', views.room_detail, name='room_detail'),
]