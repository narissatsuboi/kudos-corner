from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .models import Prize

def dashboard(request):
	# if not request.user.isAuthenticated:
	#	return #something something 404 error

	user_context = {
		# "name": request.user.name,
		# "kudos_sent": request.user.kudosSent,
		# "kudos_received": request.user.kudosReceived,      NOT YET IN MODEL
		# "current_prize"
		
		"name": "Link",
		"kudos_sent": 200,
		"kudos_received": 170,
		"current_prize": "£100"
	}

	org_context = {

	}

def profile(request):
	# if not request.user.isAuthenticated:
	#	return #something something 404 error
	
	user_context = {
		# "name": request.user.name,
		# "rank": request.user.ranking,
		# "prize_count": request.user.prizeCount
		"name": "Link",
		"rank": "1st",
		"prize_count": 2,	
	}

	org_context = {
		# "name": request.user.name,
		# "prize": request.prize.description   ????
		# account_type
		# employees
		"name": "My organization",
		"prize": "£100"
	}

	return render(request, "user/profile.html", user_context)
	# return render(request, "organization/profile.html", org_context)

	
	# if request.user.admin:
	# 	return render(request, "organization/profile.html", org_context)
	# else:
	# 	return render(request, "user/profile.html", user_context)








# to research
# csrf mechanism for the form


# If a user is logged in (aka authenticated), then you can get their info by
# accessing variables of (the CustomUser class) request.user
# so name would be request.user.name and rank would be request.user.ranking




# there is a way to force people to have to log in first, but i'll try and see if i can
# do something on that on a different branch for now, you can temporarily hardcode values
# for testing and styling

