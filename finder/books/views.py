from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,Group
import random
from django.contrib.auth.decorators import login_required
from .forms import SearchForm,AddBook
from django import forms
import re
import difflib
from difflib import get_close_matches
from admins import models as adminmod
from issues import models as issuemod
from users import models as usermod
from django.core.paginator import Paginator
# Create your views here.


def details(request,bookreq):
	try:
		bookfiltered = Book.objects.all().get(pk=bookreq)
		
		authorsfiltered = Author.objects.all().filter(book_id=bookreq)
		print(authorsfiltered.query)
		tagsfiltered = Tag.objects.all().filter(book_id = bookreq)
		issuesfiltered = issuemod.Issue.objects.all().filter(book_id = bookreq)
		bookimg = BookImage.objects.get(book=bookfiltered)
	except Book.DoesNotExist:
		return render(request,"users/oops.html",{'reason':"The book no longer exists"})
	bookcount=DeleteBookRequest.objects.all().filter(book_id=bookreq)
	disable=""
	if bookcount.count()>0:
		disable="disabled"
	
	return render(request,'books/details.html',{'bookfil':bookfiltered,'authorsfil':authorsfiltered,'tagsfil':tagsfiltered,'issuesfil':issuesfiltered,'disable':disable,'bookimg':bookimg})

def index(request):
	form = SearchForm()
	book_list_wo_image = Book.objects.all().filter(status="Accepted")
	book_list = []
	for book in book_list_wo_image:
		book_list.insert(0,(book,BookImage.objects.get(book=book)))
	return render(request,'books/index.html',{"book_list":book_list,"form":form})

def overview(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            bookreq = form.cleaned_data["search"]
            url = '/books/search/'+form.cleaned_data["search"]
            return redirect(url)
        else:
            form = SearchForm()
        return render(request,"books/index.html",{'book_list':book_list, 'form':form})


def index2(request,bookreq):
	form = SearchForm()
	
	val = re.findall(r"\[([A-Za-z0-9_,]+)\]",bookreq)	
	
	if len(val)>0:
		bookids = []
		booktags = []
		book_list = []
		if len(val)>1:
			for eachval in val:					
				booktags.append(Tag.objects.all().filter(tag__contains=eachval))
			for eachtag in booktags:
				for eachbook in eachtag:
					if Book.objects.all().get(pk=eachbook.book_id).status=='Accepted':
						book_list.insert(0,(Book.objects.all().get(pk=eachbook.book_id),BookImage.objects.get(book=Book.objects.all().get(pk=eachbook.book_id))))
			booklist = list(dict.fromkeys(book_list))
			print(booklist)
			
			return render(request,'books/index2.html',{"book_list":booklist, 'form':form})
		else:
			vals = val[0].split(",")
			for eachval in vals:					
				booktags.append(Tag.objects.all().filter(tag__contains=eachval))
			for eachbook in booktags[0]:
				if Book.objects.all().get(pk=eachbook.book_id).status=='Accepted':			
					book_list.insert(0,(Book.objects.all().get(pk=eachbook.book_id),BookImage.objects.get(book=Book.objects.all().get(pk=eachbook.book_id))))
			
			for eachtag in booktags:
				booklist = []
				for eachbook in eachtag:
					if Book.objects.all().get(pk=eachbook.book_id).status=='Accepted':					
						booklist.insert(0,(Book.objects.all().get(pk=eachbook.book_id),BookImage.objects.get(book=Book.objects.all().get(pk=eachbook.book_id))))
				
				book_list = list(set(booklist) & set(book_list))
				print(book_list)
					
		
		return render(request,'books/index2.html',{"book_list":book_list, 'form':form})
	else:
		Booklist = Book.objects.all()
		booklist = []
		for book in Booklist :
			if book.status=='Accepted':
				booklist.append(book.name)
		bookList = get_close_matches(bookreq,booklist,5,0.5)
		book_list = []
		for eachbook in bookList:
			if Book.objects.all().get(name=eachbook).status=='Accepted':
				book_list.insert(0,(Book.objects.all().get(name=eachbook),BookImage.objects.get(book=Book.objects.all().get(name=eachbook)))) 
		return render(request,'books/index2.html',{"book_list":book_list, 'form':form})


@login_required
def addbook(request):
	if request.method=="POST":
		form = AddBook(request.POST,request.FILES)
		if form.is_valid():
			book_name = form.cleaned_data['book_name']
			book_author = form.cleaned_data['book_author']
			book_link = form.cleaned_data['book_link']
			linkcount = Book.objects.all().filter(link=book_link)
			if linkcount.count()>0:
				return render(request,'books/bookpresent.html',{"book_list":linkcount})
			book_tags = form.cleaned_data['book_tags']
			book_edition = form.cleaned_data['book_edition']
			book_image = form.cleaned_data['book_image']
			allUsers = User.objects.filter(groups__name="Admin")|User.objects.filter(username="superuser")	
			randomadmin = random.choice(allUsers)
			book=Book(link=book_link,name=book_name,added_by_id=request.user.id,edition=book_edition,assigned_admin=randomadmin)
			book.save()
			bookimage = BookImage(book=book)
			if book_image:
				bookimage.image=book_image
			else:
				bookimage.image="images/npa.png"
			bookimage.save()
			bookid = Book.objects.all().get(link=book_link).book
			
			if "," in book_tags :
				booktag= book_tags.split(",")
				for eachtag in booktag :
					tags=Tag(book = book, tag=eachtag)
					tags.save()			
			else:			
				tags=Tag(book = book, tag=book_tags)
				tags.save()	
			if "," in book_author :
				bookauthor = book_author.split(",")
				for eachauthor in bookauthor :
					author=Author(book = book,author=eachauthor)
					author.save()
			else:
				author=Author(book = book,author=book_author)
				author.save()
			
			bookfiltered = Book.objects.all().get(link=book_link)
			bookimg = BookImage.objects.get(book=bookfiltered)
			authorsfiltered = Author.objects.all().filter(book_id=bookid)
			tagsfiltered = Tag.objects.all().filter(book_id = bookid)		
			return render(request,'books/bookadded.html',{ 'bookfil':bookfiltered, 'authorsfil':authorsfiltered, 'tagsfil':tagsfiltered,'bookimg':bookimg})
		else:
			return render(request,"users/oops.html",{'reason':form.errors})
	else:
		form = AddBook()
	return render(request,"books/addbook.html",{"form":form})
	

def start(request):
	return render(request,'index.html')
	

@login_required
def deleterequest(request,bookreq):
	bookcount=DeleteBookRequest.objects.all().filter(book_id=bookreq)
	disable=""
	
	if not Book.objects.get(book=bookreq).status=='Accepted':
		return render(request,"users/oops.html",{'reason': "The book is yet to be verified by an admin"})
	if DeleteBookRequest.objects.filter(book_id = bookreq,user = request.user).exists():
		return render(request,"users/oops.html",{'reason': "You have already requested for deletion of this book"})
	else:
		try:
			bookfiltered = Book.objects.all().get(pk=bookreq)
			bookimage = BookImage.objects.get(book=bookfiltered)
			authorsfiltered = Author.objects.all().filter(book_id=bookreq)
			tagsfiltered = Tag.objects.all().filter(book_id = bookreq)
			issuesfiltered = issuemod.Issue.objects.all().filter(book_id = bookreq)
		except Book.DoesNotExist:
			return render(request,"users/oops.html",{'reason':"The book no longer exists"})
		allUsers = User.objects.filter(groups__name="Admin")|User.objects.filter(username="superuser")	
		randomadmin = random.choice(allUsers)
		book= Book.objects.all().get(pk=bookreq)
		deletebookrequest = DeleteBookRequest(book = book,assigned_admin = randomadmin, user=request.user)
		deletebookrequest.save()
		return render(request,'books/bookdeleterequested.html',{'bookfil':bookfiltered,'authorsfil':authorsfiltered,'tagsfil':tagsfiltered,'issuesfil':issuesfiltered,'bookimage':bookimage})

@login_required
def checkbook(request,bookid,action):
	try:
		newbook = Book.objects.get(book=bookid)
	except Book.DoesNotExist:
		return render(request,"users/oops.html",{'reason':'The required book does not exist'})
	if newbook.assigned_admin==request.user:
		newbook.status=action
		newbook.save()
		return redirect('/users')
	return render(request,"users/oops.html",{'reason':'You are not authorized to perform this action'})

@login_required
def addtoliked(request,bookid):
	if not Book.objects.get(book=bookid).status=='Accepted':
		return render(request,"users/oops.html",{'reason':'This book has not been verified by an admin yet'})
	if LikedBook.objects.filter(user=request.user,book_id=bookid).exists():
		return render(request,"users/oops.html",{'reason':'This book is already in your liked list'})
	LikedBook(user=request.user,book_id=bookid).save()
	return redirect("/books/"+str(bookid))

@login_required
def removeliked(request,bookid):
	if LikedBook.objects.filter(user=request.user,book_id=bookid).exists():
		for book in LikedBook.objects.filter(user=request.user,book_id=bookid):
			book.delete()
	else:
		return render(request,"users/oops.html",{'reason':'The required book does not exist'})
	return redirect('/users')
