from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings 

class MyUser(AbstractUser):
	pass

class PublicMemo(models.Model):
	title = models.TextField()
	text = models.TextField()
	time = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey(MyUser)

class PrivateMemo(models.Model):
	title = models.TextField()
	text = models.TextField()
	time = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey(MyUser)
	
	

          