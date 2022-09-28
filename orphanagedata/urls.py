"""orphanhome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf import settings         
from django.conf.urls.static import static         

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.home),
    path('index/', views.home),
    path('contact/', views.contact),
    path('gallery/', views.gallery),
    path('about/', views.about),
    path('causes/', views.causes),
    path('causessingle/', views.causessingle),
    path('registration/', views.registration),
    path('newregistration/', views.newregistration),
    path('showregistration/', views.showregistration),
    path('sendresponse/', views.sendresponse),
    path('deleteresponse/', views.deleteresponse),
    path('showrequest/', views.showrequest),
    path('deleterequest/', views.deleterequest),
    path('login/', views.login),
    path('logindata/', views.logindata),
    path('admin1/', views.admin),
    path('user/', views.user),
    path('addchildren/', views.addchildren),
    path('deletechildren/', views.deletechildren),
    path('deletechildren1/', views.deletechildren1),
    path('updatechildren/', views.updatechildren),
    path('updatechildren1/', views.updatechildren1),
    path('finalupdate/', views.finalupdate),
    path('deleteorphan/', views.deleteorphan),
    path('showorphan/', views.showorphan),
    path('alldetail/', views.alldetail),
    path('showchildren/', views.showchildren),
    path('registerchildren/', views.registerchildren),
    path('addevent/', views.addevent),
    path('registerevent/', views.registerevent),
    path('adminshowevent/', views.adminshowevent),
    path('deleteevent/', views.deleteevent),
    path('editevent/', views.editevent),
    path('editevent1/', views.editevent1),
    path('finaleditevent/', views.finaleditevent),
    path('showevent/', views.showevent),
    path('donationform/', views.donationform),
    path('adddonor/', views.adddonor),
    path('showdonor/', views.showdonor),
    path('deletedonor/', views.deletedonor),
    path('logout/', views.logout),
    path('showmydata/', views.showmydata),
    path('addrequest/', views.addrequest),
    path('requestchild/', views.requestchild),
    path('final/', views.final),
    path('deleteuser/', views.deleteuser),
    path('showresponse/', views.showresponse),
    path('changepassword/', views.changepassword),
    path('changepassword1/', views.changepassword1),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
