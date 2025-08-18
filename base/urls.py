from django.urls import path
from . import views
from booking import views as booking_views

urlpatterns = [
    path('', views.index, name="index"),
    path('profile/<str:pk>/', views.profile_page, name="profile"),
    path('allusers/', views.UserList.as_view(), name='all-users'),
    path('success/', booking_views.booking_success, name='booking_success'),

]
