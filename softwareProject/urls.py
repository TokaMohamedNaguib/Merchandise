"""softwareProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from purchaser import pviews
from cartpage import cviews
from systemAnalyst import sviews

from shopOwner import views

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls ),
    url(r'^$', pviews.home , name='homepage'),
    #url(r'^shopOwner/askForRequest/$', views.requestPage),
   # url(r'^shopOwner/askForRequest/$', views.sendRequest),
    url(r'^purchaser/' , include('purchaser.urls') ),
    url(r'^shopOwner/' , include('shopOwner.urls') ),
    url(r'^shopOwner/(?P<user_id>[0-9]+)$', views.index, name="shopOwnerHome"),
    url(r'^purchaser/$', pviews.purchaserhome, name='purchaserhomepage'),
    url(r'^cartpage/(?P<user_id>[0-9]+)$', cviews.homecart, name="cart"),
    url(r'^cartpage/delete/(?P<user_id>[0-9]+)/(?P<product_id>[0-9]+)$', cviews.delete),
    url(r'^paymentdetails/(?P<user_id>[0-9]+)$', cviews.paymentdetails, name='paymentdetails'),
    # url(r'^contact/(?P<user_id>[0-9]+)$', cviews.contact, name='contact'),
    url(r'^analyst/', include('systemAnalyst.urls')),

    # url(r'^shopowner/signUp/$', views.signUp),

    url(r'^employee/', include('employee.urls')),
    url(r'^cartpage/', include('cartpage.urls')),
    #url(r'^login/', auth_views.login, name='login'),



  # url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

   #url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]
if settings.DEBUG:
    urlpatterns+=[url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT,}),]