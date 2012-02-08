from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^posts/$', 'posts.views.index'),
	(r'^posts/(?P<post_id>\d+)/$', 'posts.views.detail'),
    # url(r'^$', 'jobshaker.views.home', name='home'),
    # url(r'^jobshaker/', include('jobshaker.foo.urls')),

	# Login form
	(r'^login/$', 'django.contrib.auth.views.login', 
		{'template_name': 'posts/login.html'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
