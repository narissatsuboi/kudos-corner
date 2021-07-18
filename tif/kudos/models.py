import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

# https://learndjango.com/tutorials/django-custom-user-model

class CustomUser(AbstractUser):
	# user info
	name = models.CharField(max_length = 50)
	organisation = models.IntegerField(default = 0)
	email = models.CharField(max_length = 40)

	# user statistics
	ranking = models.IntegerField(default = 0)
	kudosSent = models.IntegerField(default = 0)
	kudosReceived = models.IntegerField(default = 0)
	starsReceived = models.IntegerField(default = 0)
	prizeCount = models.IntegerField(default = 0)

	def __str__(self):
		return str(self.organisation) + " - " + self.name 

class Organisation(models.Model):
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name

class Kudos(models.Model):
	date = models.DateField(default = datetime.date.today)
	sender = models.IntegerField(default = 0)
	message = models.CharField(max_length = 100, default="")
	recipient = models.IntegerField(default = 0)
	organisation = models.IntegerField(default = 0)

	def __str__(self):
		return self.id

class Prize(models.Model):
	date = models.DateField(default = datetime.date.today)
	description = models.CharField(max_length = 100)

	def __str__(self):
		return self.description
