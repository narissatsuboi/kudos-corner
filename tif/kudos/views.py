from .models import CustomUser, Organisation, Prize, Kudos
from django.http import HttpResponse
from django.shortcuts import render

def login(request):
	return render(request, "login.html")

def dashboard(request):
	# if not request.user.is_authenticated():
	# 	return render(request, "login.html")

	user_context = {
		# "name": request.user.name,
		# "kudosSent": request.user.kudosSent,
		# "kudosReceived": request.user.kudosReceived,      
		# "starsReceived": request.user.starsReceived
		# "currentPrize"
		"users": CustomUser.objects.order_by('-starsReceived')[:3],
		"name": "Link",
		# "kudosSent": 200,
		# "kudosReceived": 170,
		"starsReceived": 4,
		"ranking": "1st",
		"currentPrize": "£100",
	}
	

	# ok, so, i think we should list what we still need to do
	# my list:
	# i'll try update the rankings whenever the site is called just to be sure
	# are you still planning on working with the css? or the forms haha
	# hmm, i think the most important part is getting the forms to work
	# but for the sending kudos thing, how do you decide who to send it to?
	# username? email? id? 
	
	# i guess we can have a dropdown that displays usernames, but sends id to the db
	# not sure how to do it in here tho
	# ok


	# my list rn
	# CSS for the whole thing (basic, implement CSS grid and some borders around elements)
	# figure out forms and how to post to db from a form in django
	# log in page


	org_context = {
		# "name":
		# "currentPrize":
		"name": "myOrg",
		"currentPrize": "£100"
	}

# Switch these two to toggle user/organisation pages
	return render(request, "user/index.html", user_context)
	# return render(request, "organization/index.html", org_context)


	# if request.user.admin:
	# 	return render(request, "organization/index.html", org_context)
	# else:
	# 	return render(request, "user/index.html", user_context)

def profile(request):
	# if not request.user.isAuthenticated:
	#	return #something something 404 error
	
	user_context = {
		# "name": request.user.name,
		# "rank": request.user.ranking,
		# "prizeCount": request.user.prizeCount
		"users": CustomUser.objects.all(),
		"kudos": Kudos.objects.filter(recipient=1),
		"name": "Link",
		"rank": "1st",
		"prizeCount": 2,	
	}
	



	org_context = {
		# "name": request.user.name,
		# "prize": request.prize.description   ????
		# accountType
		# employees
		"name": "My organization",
		"prize": "£100"
	}

# Switch these two to toggle user/organisation pages
	return render(request, "user/profile.html", user_context)
	# return render(request, "organization/profile.html", org_context)


	# if request.user.admin:
	# 	return render(request, "organization/profile.html", org_context)
	# else:
	# 	return render(request, "user/profile.html", user_context)




# If a user is logged in (aka authenticated), then you can get their info by
# accessing variables of (the CustomUser class) request.user
# so name would be request.user.name and rank would be request.user.ranking

# there is a way to force people to have to log in first, but i'll try and see if i can
# do something on that on a different branch for now, you can temporarily hardcode values
# for testing and styling

