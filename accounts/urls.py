from django.urls import path
from . import views 

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('base/', views.bbs, name='base'),
]
