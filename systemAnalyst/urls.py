from django.conf.urls import url
from . import sviews

urlpatterns = [
url(r'^$', sviews.home, name='analystlist'),
url(r'^(?P<product_id>[0-9]+)/accept$', sviews.accept, name="add"),
url(r'^(?P<product_id>[0-9]+)/reject', sviews.reject, name="reject"),

]