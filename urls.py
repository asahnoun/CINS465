from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from my_app.views import HomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helloworld_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view()),
)
