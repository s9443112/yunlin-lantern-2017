"""lattern_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from lattern.views import index,home,billboard,post_detail,about,picture

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',index),
    url(r'^home/$',home),
    url(r'^billboard/$',billboard),
    url(r'^about/$',about),
    url(r'^picture$',picture),
    url(r'^post/(?P<pk>\d+)/$',post_detail, name='post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
