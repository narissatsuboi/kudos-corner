from datetime import datetime

from django.http.response import HttpResponseRedirect
from .models import CustomUser, Organisation, Prize, Kudos
from django.http import HttpResponse, request
from django.shortcuts import render, get_object_or_404
from .forms import UpdatePrizeForm

def login(request):
	return render(request, "login.html")

def dashboard(request):
	# if not request.user.is_authenticated():
	# 	return render(request, "login.html")
	user = CustomUser.objects.get(name="Matthew")
	# change this to user = request.user later on
	user_context = {
		"users": CustomUser.objects.order_by('-starsReceived')[:3],
		"name": user.name,
		"kudosSent": user.kudosSent,
		"kudosReceived": user.kudosReceived,
		"starsReceived": user.starsReceived,
		"ranking": CustomUser.objects.filter(starsReceived__gt=user.starsReceived).count() + 1,
		"currentPrize": "N/A" if not len(Prize.objects.all()) else Prize.objects.all()[0],
	}
	
	
	org_context = {
		# "name":
		# "currentPrize":
		"name": "myOrg",
		"currentPrize": "N/A" if not len(Prize.objects.all()) else Prize.objects.all()[0],
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

    # If this is a POST request then process the Form data
	if request.method == 'POST':
		form = UpdatePrizeForm(request.POST)
		if form.is_valid():
			# process data in form.cleaned_data as required
			new_description = form.cleaned_data['prize_description']
			if len(Prize.objects.all()):
				current_prize = Prize.objects.all()[0]
				current_prize.description = new_description
			else:
				current_prize = Prize(description=new_description)
			current_prize.save()
			return HttpResponseRedirect('/')
			
	else:
		# create defuault form for get request
		form = UpdatePrizeForm()


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
		"prize": "N/A" if not len(Prize.objects.all()) else Prize.objects.all()[0],
		"form": form,
	}

# Switch these two to toggle user/organisation pages
	# return render(request, "user/profile.html", user_context)
	return render(request, "organization/profile.html", org_context)



	# if request.user.admin:
	# 	return render(request, "organization/profile.html", org_context)
	# else:
	# 	return render(request, "user/profile.html", user_context)

	