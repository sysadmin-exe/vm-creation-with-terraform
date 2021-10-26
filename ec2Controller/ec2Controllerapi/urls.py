from django.conf.urls import url, include
from ec2Controllerapi import views

urlpatterns = [ 
    url(r'^/showtags', views.getInstanceTag),
    url(r'^/shutdown$', views.shutdownInstance),

]