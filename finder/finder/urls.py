"""finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from users import views as v
from books import views as b
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
path('',b.start, name='start'),
	path('addbook',b.addbook,name='addbook'),
    path('users/',include('users.urls')),
    path('admins/',include('admins.urls')),
    path('issues/',include('issues.urls')),
    path('books/',include('books.urls')),
    path('register/',v.register,name='register'),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
	
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
