from .models import CustomUser, Organisation, Prize, Kudos
from django.http import HttpResponse

def dashboard(request):
	return HttpResponse("<p>dashboard goes here.</p>")

def profile(request):
	return HttpResponse("<p>user profile goes here.</p>")
