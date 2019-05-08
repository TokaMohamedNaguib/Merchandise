from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.homeemployee,name='list'),
url(r'^add$', views.homeemployeeAdd,name='listAdd'),
url(r'^edit$', views.homeemployeeEdit,name='listEdit'),
url(r'^(?P<product_id>[0-9]+)/edit$', views.edit, name="edit"),
url(r'^(?P<product_id>[0-9]+)/delete$', views.delete, name="delete"),
url(r'^(?P<product_id>[0-9]+)/add$', views.add, name="add"),


]