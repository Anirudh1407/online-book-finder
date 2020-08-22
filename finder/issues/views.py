from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,Group
import random
from django.contrib.auth.decorators import login_required
from .forms import AddIssue
from books.forms import AddBook
from django import forms
from admins import models as adminmod
from books import models as bookmod
from users import models as usermod

# Create your views here.


@login_required
def resolveissue(request,issueid):
	try:
		resissue = Issue.objects.all().get(pk=issueid)
	except Issue.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"The issue no longer exists"})
	try:
		bookreq = resissue.book
	except bookmod.Book.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"The book no longer exists"})
	if resissue.time==1:
		assignedadmin = resissue.assigned_to_id
	else:
		assignedadmin = adminmod.AdminParent.objects.all().get(pk=resissue.assigned_to_id).creator_id
		changes = Change.objects.all().filter(issue_id=issueid)
	if assignedadmin==request.user.id:
		if request.method=="POST":
			form = AddBook(request.POST,request.FILES)
			if form.is_valid():
				newname = form.cleaned_data['book_name']
				newedition = form.cleaned_data['book_edition']
				newauthors =form.cleaned_data['book_author']
				newbooklink = form.cleaned_data['book_link']
				newtags = form.cleaned_data['book_tags']
				changeslist = []
				if not newname==bookreq.name:
					changeslist.append("Name->From:"+bookreq.name+" To:"+newname)
				if not newedition==bookreq.edition:
					changeslist.append("Edition->From:"+str(bookreq.edition)+" To:"+str(newedition))
				if not newbooklink==bookreq.link:
					changeslist.append("Link->From:"+bookreq.link+" To:"+newbooklink)
				if form.cleaned_data['book_image']:

					changeslist.append("Image->From:"+str(bookmod.BookImage.objects.get(book=bookreq).image)+" to the current image")
					curimg = bookmod.BookImage.objects.get(book=bookreq)
					curimg.delete()
					newbookimage = bookmod.BookImage(book=bookreq)
					newbookimage.image=form.cleaned_data['book_image']
					newbookimage.save()
				newtagslist = newtags.split(',')
				
				
				for tag in bookmod.Tag.objects.all().filter(book=bookreq):
					if not tag.tag in newtagslist:
						changeslist.append("Deleted tag:"+tag.tag)
				oldtagslist = bookmod.Tag.objects.all().filter(book=bookreq)
				oldtags = []
				for tag in oldtagslist:
					oldtags.append(tag.tag)
				for tag in newtagslist:
					if not tag in oldtags:
						changeslist.append("Added tag:"+tag)
				for change in changeslist:
					Change(issue_id = issueid,change=change).save()			
				newauthslist = newauthors.split(',')
				for author in bookmod.Author.objects.all().filter(book=bookreq):
					if not author.author in newauthslist:
						changeslist.append("Deleted author:"+author.author)
				oldauthorslist = bookmod.Author.objects.all().filter(book=bookreq)
				oldauthors = []
				for author in oldauthorslist:
					oldauthors.append(author.author)
				for author in newauthslist:
					if not author in oldauthors:
						changeslist.append("Added author:"+author)
				bookreq.name = newname
				bookreq.edition = newedition
				bookreq.link = newbooklink
				bookmod.Tag.objects.all().filter(book=bookreq).delete()
				for tag in newtagslist:
					bookmod.Tag(book=bookreq,tag=tag).save()
				bookmod.Author.objects.all().filter(book=bookreq).delete()
				for author in newauthslist:
					bookmod.Author(book=bookreq,author=author).save()
				form = AddBook(initial={'book_name':bookreq.name,'book_edition':bookreq.edition,'book_author':newauthors,'book_link':bookreq.link,'book_tags':newtags})
				
				if resissue.time==1 and not request.user.is_superuser:
					resissue.status = "resolvedcheck"
				else:
					resissue.status = "resolved"
				resissue.save()
				return render(request,"issues/issueresolver.html",{'issue':resissue,'form':form,'bookreq':bookreq,'bookimg':bookmod.BookImage.objects.get(book=bookreq)})
			else:
				return render(request,"users/oops.html",{'reason':"Some error occurred!Please try again later"})
			
		else:
			tags = []
			for tag in bookmod.Tag.objects.all().filter(book=bookreq):
				tags.append(tag.tag)
			authors = []
			for author in bookmod.Author.objects.all().filter(book=bookreq):	
				authors.append(author.author)
			
			changes = []
			form = AddBook(initial={'book_name':bookreq.name,'book_edition':bookreq.edition,'book_author':",".join(map(str,authors)),'book_link':bookreq.link,'book_tags':",".join(map(str,tags))})
			return render(request,"issues/issueresolver.html",{'issue':resissue,'form':form,'changes':changes,'bookreq':bookreq,'bookimg':bookmod.BookImage.objects.get(book=bookreq)})
	else:
		return render(request,'users/oops.html',{'reason':'You are not authorized to perform this action'})
	

@login_required
def issuenotresolved(request,issueid):
	try:
		issueobj = Issue.objects.all().get(pk=issueid)
	except Issue.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"The issue no longer exists"})
	if issueobj.added_by_id==request.user.id:
		assignedadmin = issueobj.assigned_to
		newassignedadminobj = adminmod.AdminParent.objects.all().get(pk=assignedadmin)
		newassignedadmin = newassignedadminobj.creator_id
		issueobj.time = 2
		issueobj.status="unresolved"
		issueobj.save()
		return redirect("/users/"+request.user.username+"")
	else:
		return render(request,'users/oops.html',{'reason':'You are not authorized to perform this action'})


@login_required
def issuedetails(request,issueid):
	try:
		issue = Issue.objects.all().get(pk=issueid)
	except Issue.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"The issue no longer exists"})
	return render(request,'issues/issuedetails.html',{'issuedesc':issue.description,'issuebook':bookmod.Book.objects.all().get(book=issue.book_id).name,'issueadder':User.objects.all().get(pk=issue.added_by_id).username})


@login_required
def issueresolved(request,issueid):
	try:
		issue = Issue.objects.all().get(pk=issueid)
	except Issue.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"The issue no longer exists"})
	if request.user.id==issue.added_by_id:
		issue.status = "resolved"
		issue.save()
		return redirect("/users/"+request.user.username+"/resolvedissues")
	else:
		return render(request,"users/oops.html",{'reason':"You are not authorized to perform this action"})

@login_required
def showissue(request,bookfil):
	return render(request,"issues/showissues.html",{'allissues':Issue.objects.all().filter(book_id=bookfil,status="resolvedcheck")|Issue.objects.all().filter(book_id=bookfil,status="unresolved"),'bookfil':bookfil})

@login_required
def addissue(request,bookfil):
	if not bookmod.Book.objects.get(book=bookfil).status=='Accepted':
		return render(request,"users/oops.html",{'reason':'This book is yet to be verified by an admin'})
	if request.method=="POST":
		form = AddIssue(request.POST)
		if form.is_valid():
			allUsers = User.objects.filter(groups__name="Admin").union(User.objects.filter(is_superuser=True))
			randomadmin = random.choice(allUsers)
			Issue(book_id = bookfil,description = form.cleaned_data["description"],assigned_to = randomadmin,added_by = request.user).save()
			return redirect("/books/"+str(bookfil))
	else:
		return render(request,"issues/addissue.html",{'form':AddIssue(),'bookfil':bookfil})




