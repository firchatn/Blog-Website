from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email =  models.EmailField()
    phone = models.CharField(max_length=20)
    #is_reviewed = models.BooleanField(default=False)
    img = models.ImageField(upload_to='upload/')
    joind_date = models.DateTimeField(
        'date published', auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name


class Article(models.Model):
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=20)
	desc = models.CharField(max_length=300)
	aboutnow = models.CharField(max_length=3000)
	img = models.ImageField(upload_to='upload/')
	post_date = models.DateTimeField('date published', auto_now_add=True, auto_now=False)
	def __str__(self):
		return self.title