from datetime import datetime
from django.shortcuts import render
from django.core.checks import messages
from django.http import HttpResponse, request
from django.http.response import HttpResponseRedirect
from .models import CustomUser, Organisation, Prize, Kudos
from .forms import UpdatePrizeForm, SendKudoForm, RateKudoStars

def login(request):
	return render(request, "login.html")

def dashboard(request):
	# if not request.user.is_authenticated():
	# 	return render(request, "login.html")
	
	user = CustomUser.objects.get(name="Matthew")
	# change to user = request.user later on
	organisation = Organisation(name="My Organisation")
	
	is_organisation = False # change to check whether user is admin in the future
	
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
		"name": organisation.name,
		"currentPrize": "N/A" if not len(Prize.objects.all()) else Prize.objects.all()[0],
	}

	if is_organisation:
		return render(request, "organization/index.html", org_context)
	return render(request, "user/index.html", user_context)

def profile(request):
	# if not request.user.isAuthenticated:
	#	return render(request, "login.html")
	
	user = CustomUser.objects.get(name="Matthew")
	organisation = Organisation(name="My Organisation")
	# change to user = request.user later on

	is_organisation = False # change to check whether user is admin in the future

	if request.method == 'POST':
		if is_organisation:
			form = UpdatePrizeForm(request.POST)
			if form.is_valid():
				new_description = form.cleaned_data['prize_description']
				if len(Prize.objects.all()):
					current_prize = Prize.objects.all()[0]
					current_prize.description = new_description
				else:
					current_prize = Prize(description=new_description)
				current_prize.save()
				return HttpResponseRedirect('/')
		else:
			if "sendKudos" in request.POST:
				form = SendKudoForm(request.POST)
				if form.is_valid():
					# add a new kudo to the database
					message = form.cleaned_data['message']
					recipient = form.cleaned_data['recipient']
					new_kudos = Kudos(message=message, sender=user.id, recipient=recipient)
					new_kudos.save()
					# increment kudos sent for user
					user.kudosSent += 1
					user.save()
					# increment kudos received by recepient
					recipientUser = CustomUser.objects.get(id=recipient)
					recipientUser.kudosReceived += 1
					recipientUser.save()
			else:
				form = RateKudoStars(request.POST)
				if form.is_valid():
					kudoId = form.cleaned_data['id']
					rating = form.cleaned_data['rating']
					print(kudoId, rating)
					currentKudo = Kudos.objects.get(id=kudoId)
					# give rating to recipient
					recipient = currentKudo.recipient
					recipientUser = CustomUser.objects.get(id=recipient)
					recipientUser.starsReceived += rating
					recipientUser.save()
					# remove kudo from database
					currentKudo.delete()
			return HttpResponseRedirect('/profile')
			
	else:
		# create default forms for get request
		send_kudos_form = SendKudoForm()
		rate_kudos_form = RateKudoStars()
		prize_form = UpdatePrizeForm()

	user_context = {
		"name": user.name,
		"rank": CustomUser.objects.filter(starsReceived__gt=user.starsReceived).count() + 1,
		"prizeCount": user.prizeCount,
		"users": CustomUser.objects.all(),
		"kudos": Kudos.objects.filter(recipient=user.id),
		"sendKudosForm": send_kudos_form,
		"rateKudosForm": rate_kudos_form,
	}

	org_context = {
		"name": organisation.name,
		"prize": "N/A" if not len(Prize.objects.all()) else Prize.objects.all()[0],
		"form": prize_form,
	}

	if is_organisation:
		return render(request, "organization/profile.html", org_context)
	return render(request, "user/profile.html", user_context)