
from django.conf.urls import url
from purchaser import pviews
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth import views as auth_views

app_name= 'purchaser'

urlpatterns = [


    url(r'^signUp$', pviews.signUp, name="Signup"),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page':'purchaser:login'},name='logout'),
    url(r'^add/(?P<user_id>[0-9]+)/(?P<product_id>[0-9]+)$', pviews.add, name=""),
    url(r'^details/(?P<product_id>[0-9]+)$', pviews.details, name="details"),

    url(r'^search$', pviews.search, name='search'),
    url(r'^searchprice$', pviews.searchprice, name='searchprice'),
    url(r'^searchcategory$', pviews.searchcategory, name='searchcategory'),
    url(r'^comment/(?P<product_id>[0-9]+)$', pviews.addComment),
    url(r'^rating/(?P<product_id>[0-9]+)$', pviews.rating)

]
