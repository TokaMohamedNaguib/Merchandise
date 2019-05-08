from django.conf.urls import url


from shopOwner import views
from django.contrib.auth import views as auth_views
urlpatterns = [
     url(r'^signUpp$', views.signUpp, name="Signupp"),

     url(r'^askForRequest/(?P<user_id>[0-9]+)$',views.create,name="create"),

]