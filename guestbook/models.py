from django.db import models
from django.conf import settings

# Create your models here.

class TextMessage(models.Model):
	talker = models.CharField(max_length = 20, blank = False)
	message = models.CharField(max_length = 50, blank = True)
	def __str__(self):
		return self.talker + " " + self.message

class PictureMessage(models.Model):
	link = models.CharField(max_length = 1000)
	def __str__(self):
		return self.link

class reaction(models.Model):
	talker = models.CharField(max_length = 10000)
	message = models.CharField(max_length = 10000)
	time = models.CharField(max_length = 10000)
	def __str__(self):
		return self.talker + " " + self.message + " " + self.time