from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .models import Prize

def dashboard(request):
	return HttpResponse("<p>dashboard goes here.</p>")

def profile(request):
	context = {
		# "name": request.user.name,
		# "rank": request.user.ranking,
		"name": "Link",
		"rank": "1st",
		"prize_count": 2,
		
	}
	return render(request, "user/profile.html", context)


# to research
# csrf mechanism for the form




# If a user is logged in (aka authenticated), then you can get their info by
# accessing variables of (the CustomUser class) request.user
# so name would be request.user.name and rank would be request.user.ranking

# ok, I see. How will we set it up so that a user is logged in? I.e. how can 
#  i actually see those values on the page




