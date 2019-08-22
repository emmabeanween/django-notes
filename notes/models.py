from django.db import models
from django.utils.timezone import now


class User(models.Model):
	username = models.CharField(max_length=40)
	password = models.CharField(max_length = 40)
	user_id = models.IntegerField()


class Note(models.Model):
	title = models.CharField(max_length = 100)
	content = models.CharField(max_length = 5000)
	note_id = models.CharField(max_length = 10)
	date_updated = models.DateTimeField(default=now)
	user_created = models.CharField(max_length=40)






