from django.conf.urls import include, url
from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns =[
              url(r'^$', views.home),
              url(r'^all/$', views.all_bands),
              url(r'^(?P<band_id>\d+)/$', views.band),
              url(r'^api/(?P<pk>\d+)/$', views.band_detail.as_view()),
              ]

urlpatterns = format_suffix_patterns(urlpatterns)
