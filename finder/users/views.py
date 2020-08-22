from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm,ReportUser,ProfileChange
from django.contrib.auth.decorators import login_required
import datetime
from datetime import date
from django.http import HttpResponseRedirect
from books import models as bookmod
import random
from admins import models as adminmod
from issues import models as issuemod
from django.db.models import F
from admins import views as adviews


# Create your views here.

@login_required
def profile(request,userreq):
	try:
		userid = User.objects.all().get(username = userreq).id	
	except User.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"The user does not exist"})	
	profile_filtered = UserProfile.objects.all().get(pk=userid)
	is_admin = User.objects.all().get(username = userreq).groups.filter(name="Admin").exists() or User.objects.all().get(username = userreq).is_superuser
	is_req_admin = request.user.groups.filter(name="Admin").exists() or request.user.is_superuser
	bannedadmin = False
	rejectedadmin = False
	lefttimebannedadmin = 0
	lefttimerejectedadmin = 0

	livesleft = 0
	if adminmod.BannedAdmin.objects.filter(pk = userid):
		rejectiondate = adminmod.BannedAdmin.objects.all().get(pk = userid).rejection_date
		timeelapsed = rejectiondate.date()-datetime.date.today()
		if timeelapsed.days<30:
			bannedadmin = True
			lefttimebannedadmin = 30-timeelapsed.days

		else:
			BannedAdmin.objects.all().get(pk = userid).delete()
			bannedadmin = False	
		
	if adminmod.RejectedAdmin.objects.filter(pk = userid):
		rejectiondate = adminmod.RejectedAdmin.objects.all().get(pk = userid).rejection_date
		timeelapsed = rejectiondate-datetime.date.today()
		if timeelapsed.days<14:
			lefttimerejectedadmin = 14 - timeelapsed.days
			rejectedadmin = True
		else:
			RejectedAdmin.objects.all().get(pk = userid).delete()
			rejectedadmin = False
	banneduser = BannedUser.objects.filter(pk=userid).exists()
	admin_eligibility = False
	if (not adminmod.AdminRequest.objects.all().filter(pk=userid).exists()) and (not is_admin) and not bannedadmin and not rejectedadmin and not banneduser:
		admin_eligibility = True
	banneduser = False

	if BannedUser.objects.filter(user_id=userid).exists():
		banneduser = True

	return render(request,"users/profile.html",{'profilefil':profile_filtered,'username':userreq,'is_admin':is_admin,'admin_eligibility':admin_eligibility,'is_req_admin':is_req_admin,'banneduser':banneduser,'bannedadmin':bannedadmin,'rejectedadmin':rejectedadmin,'lefttimebannedadmin':lefttimebannedadmin,'lefttimerejectedadmin':lefttimerejectedadmin})

def register(request):
	if request.method=="POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			
			emailid=form.cleaned_data['email']
			emailcheck=UserProfile.objects.all().filter(email=emailid)
			if emailcheck.count()>0:
				return render(request,"users/oops.html",{"reason":"user account is already existing with the email"})
			if form.cleaned_data['username']=='profilechange':
				return render(request,"users/oops.html",{'reason':'This profile name is already taken'})
			new_user = form.save()
			User.objects.all().get(username=form.cleaned_data['username']).email = form.cleaned_data['email']
			newuserprofile = UserProfile(user = new_user,creation_date = datetime.date.today(),gender = form.cleaned_data.get('gender'),name = form.cleaned_data.get('name'),dob = form.cleaned_data.get('dob'),country = form.cleaned_data.get('country'),email = form.cleaned_data['email'])
			
			
			newuserprofile.save()
			new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
			login(request,new_user)
			url = '/users/'+ form.cleaned_data.get('username')
			return redirect(url)
	else:
		form = RegisterForm()
	return render(request,"users/register.html",{"form":form})

@login_required
def reportuser(request,issueid,usertype):
	issueobj = None
	deleteobj = None
	try:
		if usertype=='issuer':
			issueobj = issuemod.Issue.objects.all().get(pk=issueid)
		elif usertype=='deleter':
			deleteobj = bookmod.DeleteBookRequest.objects.get(pk = issueid)
		else:
			bookobj = bookmod.Book.objects.get(book=issueid)
			bookobj.status='Rejected'
			bookobj.save()		
			bookobj = bookmod.Book.objects.get(book=issueid)
	except issuemod.Issue.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"The book either does not exist or has been deleted"})
	except bookmod.DeleteBookRequest.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"The request either does not exist or has been deleted"})
	except bookmod.Book.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"The book either does not exist or has been deleted"})
	if usertype=='issuer':
		if issueobj.time==1:
			assignedadmin = issueobj.assigned_to_id
		else:
			assignedadmin = adminmod.AdminParent.objects.all().get(pk=issueobj.assigned_to_id).creator_id
	elif usertype=='deleter':
		assignedadmin = deleteobj.assigned_admin.id
	else:
		assignedadmin = bookobj.assigned_admin_id
	if assignedadmin==request.user.id:
		if(request.method=="POST"):
			if usertype=='issuer':
				issueusername = User.objects.all().get(pk = issueobj.added_by_id).username
				if issueusername=='superuser':
					return render(request,"users/oops.html",{'reason':'You cannot report the superuser'})
				if issueusername=='deletedusers':
					return render(request,"users/oops.html",{'reason':"The user's account is already deleted"})
			if usertype=='adder':
				bookid = issueid
				issueusername = bookmod.Book.objects.all().get(pk = bookid).added_by.username
				if issueusername=='superuser':
					return render(request,"users/oops.html",{'reason':'You cannot report the superuser'})
				if issueusername=='deletedusers':
					return render(request,"users/oops.html",{'reason':"The user's account is already deleted"})
			if usertype=='deleter':
				issueuser= bookmod.DeleteBookRequest.objects.all().get(pk = issueid).user_id
				issueusername = User.objects.all().get(pk = issueuser).username
				if issueusername=='superuser':
					return render(request,"users/oops.html",{'reason':'You cannot report the superuser'})
				if issueusername=='deletedusers':
					return render(request,"users/oops.html",{'reason':"The user's account is already deleted"})
			form = ReportUser(request.POST)
			if issueobj:
				reportexists = ReportedUser.objects.filter(user_id = issueobj.added_by_id,reporting_admin_id = request.user.id,issue=issueobj).exists()
			elif deleteobj:
				reportexists = ReportedUser.objects.filter(user_id = deleteobj.user.id,reporting_admin_id = request.user.id,deleterequest=deleteobj).exists()
			else:
				reportexists = ReportedUser.objects.filter(user_id = bookobj.added_by_id,reporting_admin_id = request.user.id,bookadder=bookobj).exists()
			if form.is_valid():
				if not reportexists:
					if issueobj:
						
						newuserreport = ReportedUser(user_id = User.objects.get(username=issueusername).id,comment = form.cleaned_data['comment'],reporting_admin_id = request.user.id,issue_id = issueid)
					elif deleteobj:
						newuserreport = ReportedUser(user_id = User.objects.get(username=issueusername).id,comment = form.cleaned_data['comment'],reporting_admin_id = request.user.id,deleterequest_id = issueid)
					else:
						newuserreport = ReportedUser(user_id = User.objects.get(username=issueusername).id,comment = form.cleaned_data['comment'],reporting_admin_id = request.user.id,bookadder_id = issueid)
					newuserreport.save()
					for reason in request.POST.getlist('reason'):
						UserReason(reason=reason,reporteduser = newuserreport).save()
					if request.user.is_superuser:
						return banuser(request,issueusername,request.user.username,"userreport")
					return redirect('/users/'+request.user.username+'/pendingissues')
				else:
					return render(request,"users/oops.html",{"reason":"This user has already been reported"})
		else:
			if usertype=='issuer':
				issueusername = User.objects.all().get(pk = issueobj.added_by_id).username
				if issueusername=='superuser':
					return render(request,"users/oops.html",{'reason':'You cannot report the superuser'})
				if issueusername=='deletedusers':
					return render(request,"users/oops.html",{'reason':"The user's account is already deleted"})
			if usertype=='adder':
				bookid = issueid
				issueusername = bookmod.Book.objects.all().get(pk = bookid).added_by.username
				if issueusername=='superuser':
					return render(request,"users/oops.html",{'reason':'You cannot report the superuser'})
				if issueusername=='deletedusers':
					return render(request,"users/oops.html",{'reason':"The user's account is already deleted"})
			if usertype=='deleter':
				issueuser= bookmod.DeleteBookRequest.objects.all().get(pk = issueid).user_id
				issueusername = User.objects.all().get(pk = issueuser).username
				if issueusername=='superuser':
					return render(request,"users/oops.html",{'reason':'You cannot report the superuser'})
				if issueusername=='deletedusers':
					return render(request,"users/oops.html",{'reason':"The user's account is already deleted"})
			form = ReportUser()
		return render(request,"users/userreporter.html",{"report_form":form,"issueid":issueid,'usertype':usertype})
	else:
		return render(request,"users/oops.html",{"reason":"You are not authorized to perform this action"})


@login_required
def removereport(request,reporteduser,reportingadmin):
	reportobjexists = ReportedUser.objects.filter(user_id=User.objects.all().get(username=reporteduser).id,reporting_admin_id = User.objects.all().get(username=reportingadmin).id ).exists()
	if reportobjexists:
		reportobj = ReportedUser.objects.all().get(user_id=User.objects.all().get(username=reporteduser).id,reporting_admin_id = User.objects.all().get(username=reportingadmin).id )
		if adminmod.AdminParent.objects.get(pk = User.objects.all().get(username=reportingadmin)).creator_id == request.user.id:
			reportobj.delete()
			return redirect("/users/"+request.user.username+'/reportedusers')
		else:
			return render(request,'users/oops.html',{"reason":"You do not have permission to perform this action"})
	else:
		return render(request,'users/oops.html',{"reason":"This action has already been performed OR the report does not exist"})

@login_required
def home(request):
	url = '/users/'+request.user.username
	return redirect(url)

@login_required
def deleteconfirm(request,userreq):
	if request.user.username==userreq:
		return render(request,"users/delete.html")
	return render(request,'users/oops.html',{"reason":"You do not have permission to perform this action"})


@login_required
def delete(request,userreq):
	userid = User.objects.all().get(username=userreq).id
	if User.objects.all().get(username=userreq).is_superuser:
		return render(request,"users/oops.html",{'reason':'You cannot delete the superuser'})
	if not request.user.username==userreq:
		if request.user.groups.filter(name="Admin").exists() or request.user.is_superuser:
			if BannedUser.objects.filter(user_id = userid,time=1).exists():
				deletehelper(userreq,userid)
				User.objects.get(username=userreq).delete()
				return redirect('/users')
			else:
				return render(request,"users/oops.html",{'reason':"You are not authorized to perform this action"})
		else:
			return render(request,"users/oops.html",{'reason':"You are not authorized to perform this action"})
	else:
		deletehelper(userreq,userid)
		User.objects.get(username=userreq).delete()
		return redirect('/accounts/login')

def deletehelper(userreq,userid):
	if User.objects.get(username=userreq).groups.filter(name = 'Admin'):
		adviews.deleteadmin(userreq)
	if adminmod.ReportedAdmin.objects.filter(admin_id=userid).exists():
		adminmod.ReportedAdmin.objects.all().get(admin_id=userid).delete()
	if ReportedUser.objects.filter(user_id = userid).exists():
		ReportedUser.objects.all().filter(user_id= userid).delete()
	booksadded = bookmod.Book.objects.all().filter(added_by_id=userid)
	for book in booksadded:
		book.added_by_id = User.objects.get(username="deletedusers").id 
		book.save()


@login_required
def profileredirect(request,userreq,itemreq):
	try:
		userid = User.objects.all().get(username = userreq).id	
	except User.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"The user does not exist"})
	context={}
	empty = False
	if itemreq=="resolvedissues":
		issues_asked_resolved_first = issuemod.Issue.objects.all().filter(added_by_id=userid,status="resolved",time=1)
		issues_asked_resolved_second = issuemod.Issue.objects.all().filter(added_by_id=userid,status="resolved",time =2)
		issues_asked_resolved_check_pending = issuemod.Issue.objects.all().filter(added_by_id=userid,status="resolvedcheck",time =1)
		if not (issues_asked_resolved_first or issues_asked_resolved_second or issues_asked_resolved_check_pending):
			empty = True
		context={'issues_asked_resolved_first':issues_asked_resolved_first,'issues_asked_resolved_second':issues_asked_resolved_second,'issues_asked_resolved_check_pending':issues_asked_resolved_check_pending}
	elif itemreq=='checkbook':
		checkbooklist = bookmod.Book.objects.filter(assigned_admin_id=userid,status='checking')
		context={'checkbooklist':checkbooklist}
		if not checkbooklist:
			empty = True
	elif itemreq=='likedbooks':
		likedbooks = bookmod.LikedBook.objects.filter(user_id = userid)
		if not likedbooks:
			empty = True
		context={'likedbooks':likedbooks}
			
	elif itemreq=="unresolvedissues":
		issues_asked_unresolved_first_ask = issuemod.Issue.objects.all().filter(added_by_id=userid,status="unresolved",time= 1)
		issues_asked_unresolved_second_ask = issuemod.Issue.objects.all().filter(added_by_id=userid,status="unresolved",time= 2)
		if not (issues_asked_unresolved_first_ask or issues_asked_unresolved_second_ask):
			empty = True
		context={'issues_asked_unresolved_first_ask':issues_asked_unresolved_first_ask,'issues_asked_unresolved_second_ask':issues_asked_unresolved_second_ask}
	elif itemreq=="booksadded":
		books_filtered = bookmod.Book.objects.all().filter(added_by_id=userid)
		context={'booksfil':books_filtered}
		if not books_filtered:
			empty = True
	elif itemreq=='bookspending':
		bookspending = bookmod.Book.objects.filter(added_by_id=userid,status='checking')|bookmod.Book.objects.filter(added_by_id=userid,status='Rejected')
		context={'bookspending':bookspending}
		if not bookspending:
			empty=True
	elif itemreq=="reissues":
		createdadminissues = []
		for eachissue in issuemod.Issue.objects.all():
			if eachissue.time==2 and adminmod.AdminParent.objects.all().get(created_id = eachissue.assigned_to_id).creator_id==userid and eachissue.status=="unresolved":
				createdadminissues.append(eachissue)
		if not createdadminissues:
			empty = True
		context={'createdadminissues':createdadminissues}
	elif itemreq=="adminrequest":
		adminrequestsfiltered = adminmod.AdminRequest.objects.all().filter(assigned_to_id=userid)
		adminreqfil = []
		for adreq in adminrequestsfiltered:
			adminreqfil.append(User.objects.all().get(pk = adreq.user_id).username)
		if not adminreqfil:
			empty = True
		context={'adminreqfil':adminreqfil}
	elif itemreq=="pendingissues":
		issues_pending = issuemod.Issue.objects.all().filter(assigned_to_id=userid,status = "unresolved")
		if not issues_pending:
			empty = True
		context={'issues_pending':issues_pending}
		
	elif itemreq=="deleterequest":
		deletereq_pending = bookmod.DeleteBookRequest.objects.all().filter(assigned_admin_id=userid)
		if not deletereq_pending:
			empty = True
		context['deletereq_pending']=deletereq_pending	
		
	elif itemreq=="reportedusers":
		adminsavbforreporting = adminmod.AdminParent.objects.all().filter(creator_id=userid)
		adminids = []
		for admin in adminsavbforreporting:
			adminids.append(admin.created_id)
		reportedusers = ReportedUser.objects.all().filter(reporting_admin_id__in = adminids)
		reporteduserdetails = []
		for users in reportedusers:
			reporteduserdetails.insert(0,(User.objects.all().get(pk=users.user_id).username,User.objects.all().get(pk=users.reporting_admin_id).username))
		if not reportedusers:
			empty = True
		context={'reportedusers':reportedusers,'reporteduserdetails':reporteduserdetails}
	elif itemreq=="adminscreated":
		adminsavbforreportingid = adminmod.AdminParent.objects.all().filter(creator_id=userid)
		print(adminsavbforreportingid.query)
		adminsavbforreporting = []
		for adreq in adminsavbforreportingid:
				adminsavbforreporting.append((User.objects.all().get(pk = adreq.created_id).username,User.objects.all().get(pk = adreq.created_id).last_login))
		context={'adminsavbforreporting':adminsavbforreporting}
		if not adminsavbforreporting:
			empty = True
	elif itemreq=="reportedadmins":
		directcreatedadmins = adminmod.AdminParent.objects.all().filter(creator_id=userid)
		secondorderadmin = []
		for admin in directcreatedadmins:
			seconddirectcreatedadmins = secondorderadmin.extend(adminmod.AdminParent.objects.all().filter(creator_id=admin.created_id))
		secondorderadminusernames = []
		for admin in secondorderadmin:
			if adminmod.ReportedAdmin.objects.all().filter(admin_id=admin.created_id).exists():
				secondorderadminusernames.append(User.objects.all().get(pk = admin.created_id).username)
		if not secondorderadminusernames:
			empty = True
		context = {'reportedadmins':secondorderadminusernames}
	else:
		return render(request,"users/oops.html",{'reason':"The requested item does not exist"})	
	context['is_admin'] = request.user.groups.filter(name="Admin").exists() or request.user.is_superuser
	context['empty'] = empty
	return render(request,"users/dashboarditems.html",context)

@login_required
def checkuser(request,reporteduser,reportingadmin):
	try:
		report = ReportedUser.objects.all().get(user_id=User.objects.all().get(username=reporteduser).id,reporting_admin_id = User.objects.all().get(username=reportingadmin).id)
	except ReportedUser.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"The report does not exist"})	
	except User.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"The user does not exist"})	
	reportedparent = adminmod.AdminParent.objects.all().get(created_id = User.objects.all().get(username=reportingadmin).id)
	if reportedparent.creator_id==request.user.id:
		reasons = []
		for userreport in UserReason.objects.filter(reporteduser=report):
			reasons.append(userreport.reason)
		changesmade = issuemod.Change.objects.all().filter(issue_id = report.issue_id)
		issueobj = None
		if report.issue:
			issueobj = issuemod.Issue.objects.all().get(pk = report.issue_id)
		elif report.deleterequest:
			issueobj = bookmod.DeleteBookRequest.objects.get(pk = report.deleterequest_id)
		if issueobj:
			bookname = bookmod.Book.objects.all().get(pk = issueobj.book_id).name
		else:
			bookname = bookmod.Book.objects.get(book = report.bookadder.book).name
		allchanges = []
		for eachchange in changesmade:
			allchanges.append(eachchange.change)
		
		return render(request,"users/showreport.html",{'report':report,'reporteduser':reporteduser,'reportingadmin':reportingadmin,'reasons':reasons,'allchanges':allchanges,'bookname':bookname})

			
	else:
		return render(request,'users/oops.html',{"reason":"You do not have permission to perform this action"})



@login_required
def banuser(request,banneduser,banningadmin,reporttype):
	try:
		user = User.objects.all().get(username = banneduser)
		banningadminobj = User.objects.all().get(username = banningadmin)
	except User.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"The user does not exist"})	
	if reporttype=="adminreport":
		try:
			adminreport = adminmod.ReportedAdmin.objects.all().get(admin_id=user.id)
			
		except adminmod.ReportedAdmin.DoesNotExist:
			return render(request,"users/oops.html",{'reason':"No such report exists anymore"})
	if reporttype=="userreport":
		try:
			userreport = ReportedUser.objects.all().get(user_id=user.id,reporting_admin_id = banningadminobj.id)
			
		except ReportedUser.DoesNotExist:
			return render(request,"users/oops.html",{'reason':"No such report exists anymore"})

	
	if request.user.is_superuser:
		reasons = getreasons(request,user,banneduser,banningadminobj,reporttype)
		if BannedUser.objects.filter(user_id=user.id).exists():
			BannedUser.objects.all().filter(user_id=user.id).update(time = F('time')+1)
			if BannedUser.objects.all().get(user_id=user.id).time==1:
				delete(request,user.username)
		else:
			newbanuser = BannedUser(user_id = user.id)
			newbanuser.save()
			if reporttype=='adminreport':
				for adrep in adminmod.AdminReason.objects.filter(reportedadmin=adminreport):
					adrep.banneduser=newbanuser
					adrep.reportedadmin=None
					adrep.save()
				adminreport.delete()
			else:
				for userrep in UserReason.objects.filter(reporteduser=userreport):
					userrep.banneduser=newbanuser
					userrep.reporteduser=None
					userrep.save()
				userreport.delete()
		return redirect("/users/"+request.user.username+"/reportedusers")

	
	if not banningadminobj.groups.filter(name="Admin").exists():
		return render(request,"users/oops.html",{'reason':"The reporting admin has been removed recently"})	
	adminparent = adminmod.AdminParent.objects.get(created=banningadminobj)
	if request.user.id==adminparent.creator_id:
		reasons = getreasons(request,user,banneduser,banningadminobj,reporttype)
		if BannedUser.objects.filter(user_id=user.id).exists():
			BannedUser.objects.all().filter(user_id=user.id).update(time = F('time')+1)
			if BannedUser.objects.all().get(user_id=user.id).time==1:
				delete(request,user.username)
		else:
			newbanuser = BannedUser(user_id = user.id)
			newbanuser.save()
			if reporttype=='adminreport':
				for adrep in adminmod.AdminReason.objects.filter(reportedadmin=adminreport):
					adrep.banneduser=newbanuser
					adrep.reportedadmin=None
					adrep.save()
				adminreport.delete()
			else:
				for userrep in UserReason.objects.filter(reporteduser=userreport):
					userrep.banneduser=newbanuser
					userrep.reporteduser=None
					userrep.save()
				userreport.delete()
		return redirect("/users/"+request.user.username+"/reportedusers")
	else:
		return render(request,'users/oops.html',{"reason":"You do not have permission to perform this action"})


def getreasons(request,user,banneduser,banningadminobj,reporttype):
	reasons = []
	if reporttype=="adminreport":
		try:
			adminreport = adminmod.ReportedAdmin.objects.all().get(admin_id=user.id)
			
		except adminmod.ReportedAdmin.DoesNotExist:
			return render(request,"users/oops.html",{'reason':"No such report exists anymore"})
		adviews.deleteadmin(banneduser)
		for reason in adminmod.AdminReason.objects.filter(reportedadmin=adminreport):
			reasons.append(reason.reason)
		
	if reporttype=="userreport":
		try:
			userreport = ReportedUser.objects.all().get(user_id=user.id,reporting_admin_id = banningadminobj.id)
			
		except ReportedUser.DoesNotExist:
			return render(request,"users/oops.html",{'reason':"No such report exists anymore"})
		for reason in UserReason.objects.filter(reporteduser=userreport):
			reasons.append(reason.reason)
		
	return reasons

@login_required
def profilechange(request):
	try:
		userobj = UserProfile.objects.get(pk = request.user.id)
	except UserProfile.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"The user does not exist"})
	if request.method=="POST":
		form = ProfileChange(request.POST)
		if form.is_valid():
			userobj.gender = form.cleaned_data["gender"]
			userobj.dob = form.cleaned_data["dob"]
			userobj.country = form.cleaned_data["country"]
			userobj.email = form.cleaned_data["email"]
			userobj.save()
			User.objects.all().get(pk=request.user.id).email = form.cleaned_data['email']
		else:
			return render(request,"users/oops.html",{'reason':"Some error has occured.Please try again later"})
		return redirect("/users/")
	else:
		form = ProfileChange(initial={'gender':userobj.gender,'dob':userobj.dob,'country':userobj.country,'email':userobj.email})
		return render(request,"users/profilechange.html",{'form':form,'userobj':User.objects.all().get(pk = request.user.id)})




















