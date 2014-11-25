from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'django_mongo_web.gcs_app.views.index'),
    url(r'^update/', 'django_mongo_web.gcs_app.views.update'),
    url(r'^delete/', 'django_mongo_web.gcs_app.views.delete'),
    # Examples:
    # url(r'^$', 'blongo.views.home', name='home'),
    # url(r'^blongo/', include('blongo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

