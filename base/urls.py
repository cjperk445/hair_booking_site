from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('profile/<str:pk>/', views.profile_page, name="profile"),
    path('allusers/', views.UserList.as_view(), name='all-users')

]
