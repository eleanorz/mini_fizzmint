from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'fizzmint.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contact', 'fizzmint.views.contact', name = 'contact'),
    url(r'^admin/', include(admin.site.urls)),
]
