"""Tourism URL Configuration

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
from django.conf.urls import url
from . import views

urlpatterns = [
    # userhandler/124/
    url(r'^(?P<user_id>[0-9]+)/$',
        views.profileDashboard, name='profileDashboard'),
    url(r'^userdetails/(?P<user_id>[0-9]+)/$',
        views.profileDetails, name='profileDetails'),
    # url(r'^tourlist/(?P<user_id>[0-9]+)/$', views.tourList, name='tourList'),
    url(r'^tourlist/$', views.tourList, name='tourList'),
    url(r'^touredit/(?P<pk>\d+)/$', views.TourUpdate.as_view(), name='tourUpdate'),
]
