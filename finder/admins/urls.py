from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 
app_name = 'admins'

urlpatterns = [
	path('<str:userreq>/adminconfirm/',views.adminconfirm,name="adminconfirm"),
	path('<str:userreq>/makeadmin',views.makeadmin,name='makeadmin'),
	path('<str:bannedadmin>/banadmin',views.banadmin,name='banadmin'),
	path('<str:removedadmin>/removeadmin',views.removeadmin,name="removeadmin"),
	path('<str:admins>/removereportadmin',views.removereportadmin,name="removereportadmin"),
	path('<str:userreq>/adminrequestconfirmed',views.adminrequestconfirmed,name="adminrequestconfirmed"),
	path('<str:userreq>/rejectadmin',views.rejectadmin,name="rejectadmin"),
	path('<str:userreq>/<str:reportedadmin>/reportedadmins',views.checkadmin,name="checkadmin"),
	path('<str:adminname>/reportadmin',views.reportadmin,name="reportadmin"),
	path('<str:delreq>/deletebook/<str:option>',views.deletebook,name="deletebook"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)	
