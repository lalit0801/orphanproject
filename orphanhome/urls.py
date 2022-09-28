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
from orphanagedata import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orphanagedata.urls')),
    path('index/', include('orphanagedata.urls')),
    path('contact/', include('orphanagedata.urls')),
    path('gallery/', include('orphanagedata.urls')),
    path('causes/', include('orphanagedata.urls')),
    path('causessingle/', include('orphanagedata.urls')),
    path('about/', include('orphanagedata.urls')),
    path('register/', include('orphanagedata.urls')),
    path('registerdata/', include('orphanagedata.urls')),
    path('showregister/', include('orphanagedata.urls')),
    path('registration/', include('orphanagedata.urls')),
    path('newregistration/', include('orphanagedata.urls')),
    path('showregistration/', include('orphanagedata.urls')),
    path('showrequest/', include('orphanagedata.urls')),
    path('sendresponse/', include('orphanagedata.urls')),
    path('deleteresponse/', include('orphanagedata.urls')),
    path('deleterequest/', include('orphanagedata.urls')),
    path('login/', include('orphanagedata.urls')),
    path('logindata/', include('orphanagedata.urls')),
    path('admin1/', include('orphanagedata.urls')),
    path('user/', include('orphanagedata.urls')),
    path('addchildren/', include('orphanagedata.urls')),
    path('showchildren/', include('orphanagedata.urls')),
    path('showorphan/', include('orphanagedata.urls')),
    path('deletechildren/', include('orphanagedata.urls')),
    path('deletechildren1/', include('orphanagedata.urls')),
    path('updatechildren/', include('orphanagedata.urls')),
    path('updatechildren1/', include('orphanagedata.urls')),
    path('finalupdate/', include('orphanagedata.urls')),
    path('deleteorphan/', include('orphanagedata.urls')),
    path('alldetail/', include('orphanagedata.urls')),
    path('registerchildren/', include('orphanagedata.urls')),
    path('donationform/', include('orphanagedata.urls')),
    path('adddonor/', include('orphanagedata.urls')),
    path('showdonor/', include('orphanagedata.urls')),
    path('deletedonor/', include('orphanagedata.urls')),
    path('addevent/', include('orphanagedata.urls')),
    path('registerevent/', include('orphanagedata.urls')),
    path('adminshowevent/', include('orphanagedata.urls')),
    path('deleteevent/', include('orphanagedata.urls')),
    path('editevent/', include('orphanagedata.urls')),
    path('editevent1/', include('orphanagedata.urls')),
    path('finaleditevent/', include('orphanagedata.urls')),
    path('showevent/', include('orphanagedata.urls')),
    path('logout/', include('orphanagedata.urls')),
    path('showmydata/', include('orphanagedata.urls')),
    path('addrequest/', include('orphanagedata.urls')),
    path('requestchild/', include('orphanagedata.urls')),
    path('final/', include('orphanagedata.urls')),
    path('deleteuser/', include('orphanagedata.urls')),
    path('finalupdate/', include('orphanagedata.urls')),
    path('showresponse/', include('orphanagedata.urls')),
    path('changepassword/', include('orphanagedata.urls')),
    path('changepassword1/', include('orphanagedata.urls')),
    
    
]
