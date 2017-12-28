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
from django.conf.urls import url, include
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from ztour.views import home, ContactView, BirdWatchingView, BookView, MessagesubmittedView
from userhandler.views import signup


urlpatterns = [
    url(r'^admin-hemco/', admin.site.urls),
    url(r'^$', home),
    url(r'^contact/', ContactView.as_view()),
    url(r'^messagesubmitted/', MessagesubmittedView.as_view()),
    #url(r'^contact/(?P<id>\d+)/', ContactView.as_view()),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', signup, name='signup'),
    url(r'^birdwatching', BirdWatchingView.as_view()),
    url(r'^book', BookView.as_view()),
]

# Change admin site title
admin.site.site_header = _("HEMCO Site Administration")
admin.site.site_title = _("HEMCO Admin")
