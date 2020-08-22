from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,Group
import random
from django.contrib.auth.decorators import login_required
from books.forms import AddBook
from django import forms
from books import models as bookmod
from admins import models as adminmod
from issues import models as issuemod
from users import models as usermod
from .forms import ReportAdmin
import datetime


# Create your views here.


@login_required
def adminconfirm(request,userreq):
	try:
		User.objects.get(username=userreq)
	except User.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"No such user exists"})
	if request.user.username==userreq and not request.user.groups.filter(name="Admin").exists():
		return render(request,"admins/admin.html")
	return redirect(request,"users/oops.html",{'reason':'You are not authorized to perform this action'})

@login_required
def adminrequestconfirmed(request,userreq):
	try:
		User.objects.get(username=userreq)
	except User.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"No such user exists"})
	if request.user.username==userreq and not request.user.groups.filter(name="Admin").exists():
		allUsers = User.objects.filter(groups__name="Admin").union(User.objects.filter(is_superuser=True))
		randomadmin = random.choice(allUsers)
		newadminrequest = AdminRequest(request.user.id,randomadmin.id)
		newadminrequest.save()
		return redirect("/users/"+request.user.username)
	else:
		return redirect(request,"users/oops.html",{'reason':'You are not authorized to perform this action'})

@login_required
def makeadmin(request,userreq):
	try:
		userid = User.objects.all().get(username = userreq).id
	except User.DoesNotExist:
		return redirect(request,"users/oops.html",{'reason':'User does not exist'})
	adminreqexists = AdminRequest.objects.filter(pk=userid).exists()
	if adminreqexists:
		if request.user.id==AdminRequest.objects.get(pk=userid).assigned_to_id:
			user = User.objects.all().get(username = userreq)
			AdminRequest.objects.get(pk=user.id).delete()
			AdminParent(created_id = userid,creator_id = request.user.id).save()
			Group.objects.get(name='Admin').user_set.add(user)
			
			return redirect("/users/"+request.user.username)
		else:
			return render(request,'users/oops.html',{'reason':"You do not have permission to perform the following action"})
	else:
		return render(request,'users/oops.html',{'reason':"This action has already been performed"})



@login_required
def removereportadmin(request,admins):
	adminid = User.objects.all().get(username = admins).id
	adminparentid = AdminParent.objects.all().get(pk = adminid).creator_id
	admingpid = AdminParent.objects.all().get(pk = adminparentid).creator_id
	try:
		reportedobj = ReportedAdmin.objects.all().get(pk=adminid)
	except ReportedAdmin.DoesNotExist:
		return redirect(request,"users/oops.html",{'reason':'No such report exists'}) 
	if request.user.id==admingpid:
		ReportedAdmin.objects.all().get(pk=adminid).delete()
	else:
		return render(request,'users/oops.html',{'reason':"You do not have permission to perform the following action"})


@login_required
def reportadmin(request,adminname):
	try:
		adminid = User.objects.all().get(username = adminname).id
	except User.DoesNotExist:
		return render(request,"users/oops.html",{'reason':'No such admin exists'}) 
	try:
		adminparentid = AdminParent.objects.all().get(pk=adminid).creator_id
	except AdminParent.DoesNotExist:
		return render(request,"users/oops.html",{'reason':'No such admin exists'}) 	
	if adminparentid==request.user.id:
		if not ReportedAdmin.objects.filter(admin_id = adminid).exists():
			if(request.method=="POST"):
				form = ReportAdmin(request.POST)
				if form.is_valid():
					newadminreport = ReportedAdmin(admin_id = User.objects.all().get(username=adminname).id,comment = form.cleaned_data['comment'])
					newadminreport.save()
					for reason in request.POST.getlist('reason'):
						AdminReason(reason=reason,reportedadmin = newadminreport).save()
					if request.user.is_superuser:
						banadmin(request,adminname)
					return redirect('/users/'+request.user.username+'/pendingissues')
			else:
				if adminname=="deletedusers" or not User.objects.all().get(username = adminname).groups.filter(name="Admin").exists():
					return render(request,'users/oops.html',{'reason':"This admin has already been banned or deleted"})
				form = ReportAdmin()
			return render(request,"admins/adminissueresolver.html",{"report_form":form,'adminname':adminname})
		else:
			return render(request,'users/oops.html',{'reason':"This action has already been performed"})
	else:
		return render(request,'users/oops.html',{reason:"You are not authorized to perform this action"})


@login_required
def removeadmin(request,removedadmin):
	try:
		deletedadminid = User.objects.all().get(username = removedadmin).id
	except User.DoesNotExist:
		return redirect(request,"users/oops.html",{'reason':'No such admin exists'}) 
	adminparentid = AdminParent.objects.all().get(pk = deletedadminid).creator_id
	if request.user.is_superuser or request.user.id==AdminParent.objects.all().get(pk = adminparentid).creator_id:
		deleteadmin(removedadmin)
		return redirect('/users/'+request.user.username+'/reportedadmins')
	else:
		return render(request,'users/oops.html',{reason:"You are not authorized to perform this action"})

def deleteadmin(removedadmin):
	deletedadminid = User.objects.all().get(username = removedadmin).id
	if ReportedAdmin.objects.filter(admin_id=deletedadminid).exists():
		ReportedAdmin.objects.all().get(admin_id=deletedadminid).delete()
	for report in usermod.ReportedUser.objects.all():
		if report.issue and report.issue.added_by_id==deletedadminid:
			report.delete()
		if report.deleterequest and report.deleterequest.user_id==deletedadminid:
			report.delete()
		if report.bookadder and report.bookadder.added_by_id==deletedadminid:
			report.delete()
	if usermod.ReportedUser.objects.filter(user_id = deletedadminid).exists():
		usermod.ReportedUser.objects.all().filter(user_id= deletedadminid).delete()
	User.objects.all().get(username = removedadmin).groups.remove(Group.objects.get(name="Admin"))
		
	allcreatedadmins = AdminParent.objects.all().filter(creator_id=deletedadminid)
	deletedadmincreator = AdminParent.objects.all().get(created_id=deletedadminid).creator_id
	allcreatedadminids = []
	for admin in allcreatedadmins:
		allcreatedadminids.append(admin.created_id)
	issuesofdeletedadmin = issuemod.Issue.objects.all().filter(assigned_to_id=deletedadminid)
	reissuesofdeletedadmin = issuemod.Issue.objects.all().filter(time = 2)
	alladminrequest = AdminRequest.objects.all().filter(assigned_to_id = deletedadminid)
	allreportedusers = usermod.ReportedUser.objects.filter(reporting_admin_id=deletedadminid).delete()
	allcheckbooks = bookmod.Book.objects.filter(assigned_admin_id = deletedadminid,status='checking')

	for admins in allcreatedadmins:
		AdminParent.objects.all().get(created_id=admins.created_id).delete()
		AdminParent(created_id = admins.created_id,creator_id = deletedadmincreator).save()
		if ReportedAdmin.objects.get(pk=admins).exists():
			ReportedAdmin.objects.get(pk=admins).delete()
	for issue in issuesofdeletedadmin:
		issue.assigned_to_id = deletedadmincreator
		issue.save()
	for issue in reissuesofdeletedadmin:
		if issue.assigned_to_id in allcreatedadminids:
			issue.assigned_to_id = deletedadmincreator
			issue.save()	
	for adreq in alladminrequest:
		adreq.assigned_to_id = deletedadmincreator
		adreq.save()
	for checkbook in allcheckbooks:
		checkbook.assigned_admin_id = deletedadmincreator
		checkbook.save()
	issuemod.Issue.objects.all().filter(added_by_id=deletedadminid).delete()
	AdminParent.objects.all().get(created_id=deletedadminid).delete()


@login_required
def checkadmin(request,userreq,reportedadmin):
	reportexists = ReportedAdmin.objects.filter(
admin_id=User.objects.all().get(username=reportedadmin)).exists()
	if reportexists:
		report = ReportedAdmin.objects.all().get(
admin_id=User.objects.all().get(username=reportedadmin).id)
		reportedadminid = User.objects.all().get(username = reportedadmin).id
		reportedadminparent = AdminParent.objects.all().get(created_id=reportedadminid).creator_id
		reportedadmingp = AdminParent.objects.all().get(created_id=reportedadminparent).creator_id
		if reportedadmingp==request.user.id:		
			reasons = []
			for reason in AdminReason.objects.filter(reportedadmin=report):
				reasons.append(reason.reason)
			return render(request,"admins/showadminreport.html",{'report':report,'reasons':reasons,'reportedadmin':reportedadmin,'reportingadmin':User.objects.all().get(pk=reportedadminparent).username})
		else:
			return render(request,'users/oops.html',{'reason':"You are not authorized to perform this action"})
	else:
		return render(request,'users/oops.html',{'reason':"This action has already been performed"})	

@login_required
def rejectadmin(request,userreq):
	try:
		userid = User.objects.all().get(username = userreq).id
	except User.DoesNotExist:
		return redirect(request,"users/oops.html",{'reason':'No such user exists'}) 
	adreqobj = AdminRequest.objects.filter(pk=userid).exists()
	if request.user.id==AdminRequest.objects.get(pk=userid).assigned_to_id:
		if adreqobj:
			AdminRequest.objects.all().get(pk=userid).delete()
			RejectedAdmin(user_id = userid,rejection_date = datetime.date.today()).save()
			return redirect("/users/"+request.user.username+"/adminrequest")
		else:
			return render(request,'users/oops.html',{"reason":"This action has possibly been completed"})
	else:
		return render(request,'users/oops.html',{"reason":"You do not have permission to perform this action"})

@login_required
def banadmin(request,bannedadmin):
	try:
		admin = User.objects.all().get(username = bannedadmin)
		ReportedAdmin.objects.all().get(admin = admin.id)
	except User.DoesNotExist:
		return render(request,"users/oops.html",{'reason':'No such admin exists'}) 
	except ReportedAdmin.DoesNotExist:
		return render(request,"users/oops.html",{'reason':'No such report exists'}) 
	if request.user.is_superuser:
		newbannedadmin = BannedAdmin(user_id = admin.id,rejection_date = datetime.date.today(),assigned_admin_id = AdminParent.objects.all().get(pk = admin.id).creator_id)
		newbannedadmin.save()
		adreasonobj = AdminReason.objects.filter(reportedadmin=ReportedAdmin.objects.all().get(admin = admin.id))
		for adreason in adreasonobj:
			adreason.bannedadmin=newbannedadmin
			adreason.reportedadmin=None
		removeadmin(request,bannedadmin)
		return redirect("/users/"+request.user.username+"/reportedadmins")
	adminparentid = AdminParent.objects.all().get(pk = admin.id).creator_id
	admingpid = AdminParent.objects.all().get(pk = adminparentid).creator_id
	if request.user.id==admingpid:
		newbannedadmin = BannedAdmin(user_id = admin.id,rejection_date = datetime.date.today(),assigned_admin_id = AdminParent.objects.all().get(pk = admin.id).creator_id)
		newbannedadmin.save()
		adreasonobj = AdminReason.objects.filter(reportedadmin=ReportedAdmin.objects.all().get(admin = admin.id))
		for adreason in adreasonobj:
			adreason.bannedadmin=newbannedadmin
			adreason.reportedadmin=None
		removeadmin(request,bannedadmin)
		return redirect("/users/"+request.user.username+"/reportedadmins")
	else:
		return render(request,'users/oops.html',{"reason":"You do not have permission to perform this action"})

@login_required
def deletebook(request, delreq, option):
	deletereq= bookmod.DeleteBookRequest.objects.all().get(pk=delreq)
	bookid=deletereq.book_id
	userreq=deletereq.assigned_admin_id
	if userreq==request.user.id:
		if deletereq.time == 1 :
			if option == "delete" :
		 		userparent = adminmod.AdminParent.objects.all().get(created_id=userreq)
		 		userparentid=userparent.creator_id
		 		deleteReq=bookmod.DeleteBookRequest.objects.all().get(pk =delreq)
		 		deleteReq.time=2
		 		deleteReq.assigned_admin_id=userparentid
		 		deleteReq.save()
			elif option == "cancel" :
		 		deletereq.delete()
		 
		elif deletereq.time == 2:
			if option == "delete" :
			 	bookdel=bookmod.Book.objects.all().get(book=bookid)
			 	bookdel.delete()
		 	
			elif option == "cancel" :
			 	deletereq.delete()
		return render(request,"books/deletebook.html",{'option' : option})
	else:
		return render(request,'users/oops.html',{"reason":"You do not have permission to perform this action"})
		

