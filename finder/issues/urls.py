from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

app_name = 'issues'

urlpatterns = [
path('<str:issueid>/resolveissue',views.resolveissue,name='resolveissue'),
path('<str:issueid>/issueresolved',views.issueresolved,name='issueresolved'),
path('<str:issueid>/issuenotresolved',views.issuenotresolved,name='issuenotresolved'),
path('<str:issueid>/issuedetails',views.issuedetails,name="issuedetails"),
path('<int:bookfil>/showissue',views.showissue,name='showissue'),
path('<int:bookfil>/addissue',views.addissue,name='addissue'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)	
