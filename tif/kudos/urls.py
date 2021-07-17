from django.urls import path
from . import views

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('profile/', views.profile, name='profile'),
	path('login/', views.login, name='login')
	
]
