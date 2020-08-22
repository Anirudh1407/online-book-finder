from django.db import models
from django.contrib.auth.models import User
from books import models as bookmod


# Create your models here.

class Issue(models.Model):
	issue = models.AutoField(primary_key = True)
	book = models.ForeignKey(bookmod.Book,on_delete=models.CASCADE)
	added_by = models.ForeignKey(User,on_delete = models.CASCADE)
	status = models.CharField(max_length = 200,default = "unresolved")
	description = models.CharField(max_length = 200,default = "No issue reported")
	assigned_to = models.ForeignKey(User,related_name='assigned_to+',on_delete=models.CASCADE)
	time = models.IntegerField(default = 1)

	def __str__(self):
		return self.description

class Change(models.Model):
	issue = models.ForeignKey(Issue,on_delete=models.CASCADE)
	change = models.CharField(max_length = 100)
