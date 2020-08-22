from django.db import models
from django.contrib.auth.models import User
from books import models as bookmod
from issues import models as issuemod

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
	creation_date = models.DateTimeField('creation_date')
	gender = models.CharField(max_length = 1)
	name = models.CharField(max_length = 200)
	dob = models.DateTimeField('date_of_birth')
	country = models.CharField(max_length = 200)
	email = models.EmailField(default="google.com")


class ReportedUser(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	reporting_admin = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reporting_admin+')
	comment = models.TextField()
	issue = models.ForeignKey(issuemod.Issue,on_delete=models.CASCADE,related_name='issue+',default=None,null=True)
	deleterequest = models.ForeignKey(bookmod.DeleteBookRequest,on_delete=models.CASCADE,related_name='deleterequest+',default=None,null=True)
	bookadder = models.ForeignKey(bookmod.Book,on_delete=models.CASCADE,related_name='bookadder+',default=None,null=True)


class BannedUser(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
	time = models.IntegerField(default = 0)

class UserReason(models.Model):
	reason = models.TextField()
	reporteduser = models.ForeignKey(ReportedUser,on_delete=models.CASCADE,null=True)
	banneduser = models.ForeignKey(BannedUser,on_delete=models.CASCADE,null=True)







