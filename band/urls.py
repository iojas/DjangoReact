from django.conf.urls import include, url
from . import views

urlpatterns =[
              url(r'^$', views.home),
              url(r'^all/$', views.all_bands),
              url(r'(?P<band_id>\d+)/$', views.band),
              ]
