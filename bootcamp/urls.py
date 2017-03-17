"""bootcamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .core import views as core_views
from .search import views as search_views
from .authentication import views as authentication_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),

    url(r'^$', core_views.home, name='home'),
    url(r'^login', auth_views.login,
        {'template_name': 'core/cover.html'}, name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', authentication_views.signup, name='signup'),

    url(r'^feeds/', include('bootcamp.feeds.urls')),
    url(r'^settings/', include('bootcamp.core.urls')),
    url(r'^articles/', include('bootcamp.articles.urls')),
    url(r'^messages/', include('bootcamp.messenger.urls')),
    url(r'^questions/', include('bootcamp.questions.urls')),
    url(r'^notifications/', include('bootcamp.activities.urls')),

    url(r'^search/$', search_views.search, name='search'),
    url(r'^network/$', core_views.network, name='network'),
    url(r'^(?P<username>[^/]+)/$', core_views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
