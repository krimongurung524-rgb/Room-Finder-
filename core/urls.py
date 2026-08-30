from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('create/', views.room_create, name='room_create'),
    path('my-page/', views.my_static_page, name='my_static_page'),
    path('search/', views.room_search, name='room_search'),
    path('<slug:slug>/', views.room_detail, name='room_detail'),
    path('<slug:slug>/edit/', views.room_update, name='room_update'),
    path('<slug:slug>/delete/', views.room_delete, name='room_delete'),
]