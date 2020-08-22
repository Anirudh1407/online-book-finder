from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 
app_name = 'users'

urlpatterns = [
	path('profilechange',views.profilechange,name='profilechange'),
	path('<str:userreq>',views.profile,name='profile'),
	path('<str:issueid>/<str:usertype>/reportuser',views.reportuser,name="reportuser"),
	path('<str:reporteduser>/<str:reportingadmin>/removereport',views.removereport,name="removereport"),
	path('',views.home,name = 'home'),	
	path('<str:userreq>/deleteconfirm',views.deleteconfirm,name='deleteconfirm'),
	path('<str:userreq>/delete',views.delete,name="delete"),
	path('<str:userreq>/<str:itemreq>',views.profileredirect,name='profileredirect'),
	path('<str:reporteduser>/<str:reportingadmin>/checkuser',views.checkuser,name='checkuser'),
	path('<str:banneduser>/<str:banningadmin>/<str:reporttype>/banuser',views.banuser,name='banuser'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)	
