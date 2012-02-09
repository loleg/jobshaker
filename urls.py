from registration import *
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Default
	(r'^$', 'posts.views.index'),

	# Posts
	(r'^posts/$', 'posts.views.index'),
	(r'^posts/(?P<post_id>\d+)/$', 'posts.views.detail'),
    # url(r'^$', 'jobshaker.views.home', name='home'),
    # url(r'^jobshaker/', include('jobshaker.foo.urls')),

	# Profile
	(r'^accounts/profile/(?P<user_id>\d+)/$', 'posts.views.profile'),
	(r'^accounts/profile/$', 'posts.views.my_profile'),
	(r'^accounts/edit/$', 'posts.views.edit_profile'),
	#(r'^users/(?P<user_username>\d+)/$', 'users.views.detail'),

	# Login form
	(r'^login/$', 'django.contrib.auth.views.login', 
		{'template_name': 'registration/login.html'}),
		
	# Registration form
	(r'^accounts/', include('registration.backends.simple.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
