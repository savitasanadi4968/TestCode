from django.conf.urls import url
from newapp import views

urlpatterns = [
    url(r'^api/newapp$', views.tutorial_list),
    url(r'^api/newapp/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/newapp/published$', views.tutorial_list_published)
]