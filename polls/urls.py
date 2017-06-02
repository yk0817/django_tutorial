from django.conf.urls import url

from . import vies

urlpatterns = [
    url(r'^$',views.index,name='index'),
]