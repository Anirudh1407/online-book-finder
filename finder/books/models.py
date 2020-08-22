
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
	book = models.AutoField(primary_key = True)
	name = models.TextField(max_length = 200,default = "No name")
	link = models.URLField(max_length = 200,default="Broken Link")
	edition=  models.IntegerField(default = 1)
	added_by = models.ForeignKey(User,on_delete=models.CASCADE)
	assigned_admin = models.ForeignKey(User,on_delete=models.CASCADE,related_name='assigned_admin+')
	status = models.CharField(max_length=200,default='checking')

	def __str__(self):
		return self.name

	
class Tag(models.Model): 
	book = models.ForeignKey(Book,on_delete=models.CASCADE)
	tag = models.CharField(max_length = 200)

	def __str__(self):
		return self.tag

class Author(models.Model):
	book = models.ForeignKey(Book,on_delete=models.CASCADE)
	author = models.CharField(max_length = 200)

	def __str__(self):
		return self.author

class DeleteBookRequest(models.Model):
	book = models.ForeignKey(Book,on_delete=models.CASCADE)
	assigned_admin = models.ForeignKey(User,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user+')
	time = models.IntegerField(default = 1)

class BookImage(models.Model):
	book = models.ForeignKey(Book,on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/',default='../media/images/npa.png')

class LikedBook(models.Model):
	book=book = models.ForeignKey(Book,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='+')

