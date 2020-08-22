from django.urls import path
from . import views
from django.contrib import admin 
from django.conf import settings 
from django.conf.urls.static import static 

  

app_name = 'books'

urlpatterns = [
	path('<int:bookid>/<str:action>/checkbook',views.checkbook,name='checkbook'),
	path('',views.index,name = 'index'),
	path('<int:bookreq>',views.details,name='details'),
	path('<int:bookid>/likedbooks',views.addtoliked,name='addtoliked'),
	path('<int:bookid>/removeliked',views.removeliked,name='removeliked'),
	path('search/',views.overview,name = 'search'),
	path('search/search/', views.overview,name='search'),
	path('search/<str:bookreq>',views.index2,name='index2' ),
	path('addbook/',views.addbook,name='addbook'),
	path('<str:bookreq>/deleterequest',views.deleterequest,name='deleterequest'),
	
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
