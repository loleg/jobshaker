from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404

from information.models import Location

from posts.models import *
from posts.forms import *

def index(request):
	latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
	return render_to_response('posts/index.html', {
		'latest_post_list': latest_post_list,
	}, context_instance=RequestContext(request))
	
def detail(request, post_id):
	try:
		p = Post.objects.get(pk=post_id)
		l_user = l_post = ''
		l_user = Location.objects.get(plz=p.user.postcode)
		if p.postcode:
			l_post = Location.objects.get(plz=p.postcode)
	except Post.DoesNotExist:
		raise Http404
	return render_to_response('posts/detail.html', {
			'post': p, 'where': l_post, 'place': l_user
		}, context_instance=RequestContext(request))

def my_profile(request):
	return profile(request, request.user.id)
			
def profile(request, user_id):
	try:
		u = UserProfile.objects.get(user=user_id)
	except UserProfile.DoesNotExist:
		raise Http404
	return render_to_response('user/detail.html', {
			'userprofile': u,
		}, context_instance=RequestContext(request))

def edit_profile(request):
	try:
		u = UserProfile.objects.get(user=request.user.id)
	except UserProfile.DoesNotExist:
		raise Http404
	form = UserProfileForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		user.save()
		return redirect(user)
	form.initial['nickname'] = u.nickname
	return render_to_response('user/edit_profile.html', {
			'userprofile': u, 'form': form
		}, context_instance=RequestContext(request))