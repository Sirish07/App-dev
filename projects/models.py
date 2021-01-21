from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length = 100)
	description = models.TextField()
	Advisors = models.TextField()
	Location = models.TextField()
	Duration = models.TextField()
	language = models.CharField(max_length = 100)
	link = models.TextField()
	image = models.FilePathField(path = '/img')
