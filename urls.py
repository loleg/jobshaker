from registration import *
from autocomplete import *
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from posts import views

admin.autodiscover()

urlpatterns = patterns('',
	# Default
	(r'^$', 'posts.views.index'),
	(r'^users/.+$', 'posts.views.index'),

	# Posts
	(r'^posts/$', 'posts.views.index'),
	(r'^posts/new$', 'posts.views.add'),
	(r'^posts/(?P<post_id>\d+)/$', 'posts.views.detail'),
	(r'^posts/(?P<post_id>\d+)/edit$', 'posts.views.edit'),
	(r'^posts/(?P<post_id>\d+)/reply$', 'posts.views.reply'),

 	# url(r'^$', 'jobshaker.views.home', name='home'),
	# url(r'^jobshaker/', include('jobshaker.foo.urls')),

	# Profile
	(r'^userprofile/(?P<userprofile_id>\d+)/$', 'posts.views.profile'),	
	(r'^userprofile/replies/$', 'posts.views.my_replies'),
	(r'^userprofile/$', 'posts.views.my_profile'),
	(r'^accounts/profile/(?P<user_id>\d+)/$', 'posts.views.user'),
	(r'^accounts/edit/$', 'posts.views.edit_profile'),
	#(r'^users/(?P<user_username>\d+)/$', 'users.views.detail'),

	# Login form
	(r'^login/$', 'django.contrib.auth.views.login', 
		{'template_name': 'registration/login.html'}),
		
	# Registration form
	(r'^accounts/', include('registration.backends.simple.urls')),
	
	# Autocomplete
	('^autocomplete/', include(views.autocomplete.urls)),
	
	# Static pages
	('^about/$', direct_to_template, { 'template': 'pages/about.html'}),
	('^links/$', direct_to_template, { 'template': 'pages/links.html'}),
	
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)
