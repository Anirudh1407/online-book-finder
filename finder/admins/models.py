from django.db import models
from django.contrib.auth.models import User
from users import models as usermod

# Create your models here.

class AdminRequest(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name='assigned_to+')


class AdminParent(models.Model):
	created = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name='creator+')

class ReportedAdmin(models.Model):
	admin = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
	comment = models.TextField()

class RejectedAdmin(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
	rejection_date = models.DateTimeField('rejection_date')

class BannedAdmin(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
	rejection_date = models.DateTimeField('rejection_date')
	assigned_admin = models.ForeignKey(User,on_delete=models.CASCADE,related_name='assigned_admin+')


class AdminReason(models.Model):
	reason = models.TextField()
	reportedadmin = models.ForeignKey(ReportedAdmin,on_delete=models.CASCADE,null=True)
	bannedadmin = models.ForeignKey(BannedAdmin,on_delete=models.CASCADE,null=True)
	banneduser = models.ForeignKey(usermod.BannedUser,on_delete=models.CASCADE,null=True)



