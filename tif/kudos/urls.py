from django.urls import path
from . import views
from .views import profile

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('profile/', views.profile, name='profile'),
	# path('base/', views.base, name='base')
]
