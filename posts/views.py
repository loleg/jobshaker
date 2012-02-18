from django.shortcuts import redirect, render_to_response, get_object_or_404
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
		if p.user.postcode:
			l_user = Location.objects.filter(plz=p.user.postcode)[0]
		if p.postcode:
			l_post = Location.objects.filter(plz=p.postcode)[0]
	except Post.DoesNotExist:
		raise Http404
	return render_to_response('posts/detail.html', {
			'post': p, 'where': l_post, 'place': l_user, 
			'replies': Reply.objects.filter(post=p), 
			'my_post': (p.user.user.id == request.user.id)
		}, context_instance=RequestContext(request))

def add(request):
	up = UserProfile.objects.get(user=request.user.id)
	form = PostForm(request.POST or None)
	if form.is_valid():
		post = form.save(commit=False)
		post.user_id = up.id
		post.save()
		return redirect('/posts/%d' % post.id)
	# Populate form
	form.initial['postcode'] = up.postcode
	return render_to_response('posts/edit_post.html', {
			'form': form
		}, context_instance=RequestContext(request))
	
def edit(request, post_id):
	up = UserProfile.objects.get(user=request.user.id)
	post = get_object_or_404(Post, id=post_id)
	form = PostForm(request.POST or None, instance=post)
	if form.is_valid():
		post = form.save(commit=False)
		post.user_id = up.id
		post.save()
		msg = "Post updated successfully"
		messages.success(request, msg, fail_silently=True)
		return redirect('/posts/%d' % post.id)
	return render_to_response('posts/edit_post.html', {
			'form': form, 'post': post
		}, context_instance=RequestContext(request))
	
def reply(request, post_id):
	try:
		up = UserProfile.objects.get(user=request.user.id)
		p = Post.objects.get(pk=post_id)
	except UserProfile.DoesNotExist:
		raise Http404
	form = ReplyForm(request.POST or None)
	if form.is_valid():
		reply = form.save(commit=False)
		reply.user_id = up.id
		reply.post_id = p.id
		reply.save()
		return redirect('/posts/%d' % p.id)
	return render_to_response('posts/edit_reply.html', {
			'post': p, 'form': form
		}, context_instance=RequestContext(request))

def my_profile(request):
	try:
		up = UserProfile.objects.get(user=request.user.id)
		return profile(request, up.id)
	except UserProfile.DoesNotExist:
		return edit_profile(request)

def my_replies(request):
	try:
		up = UserProfile.objects.get(user=request.user.id)
		myposts = Post.objects.filter(user=up)
		replies = Reply.objects.all() # TODO: how to filter this..
		myreplies = Reply.objects.select_related().filter(user=up)
		return render_to_response('user/replies.html', {
				'userprofile': up,
				'myposts': myposts, 'replies': replies, 
				'myreplies': myreplies
			}, context_instance=RequestContext(request))
	except UserProfile.DoesNotExist:
		return edit_profile(request)
			
def profile(request, userprofile_id):
	up = get_object_or_404(UserProfile, pk=userprofile_id)
	if up.postcode:
		l_user = Location.objects.filter(plz=up.postcode)[0]
	return render_to_response('user/detail.html', {
			'userprofile': up, 'location': l_user,
			'posts': Post.objects.filter(user=up), 
		}, context_instance=RequestContext(request))

def user(request, user_id):
	up = get_object_or_404(UserProfile, user=user_id)
	return profile(request, up.id)

def edit_profile(request):
	try:
		up = UserProfile.objects.get(user=request.user.id)
		form = UserProfileForm(request.POST or None, instance=up)
	except UserProfile.DoesNotExist:
		form = UserProfileForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		user.user_id = request.user.id
		user.save()
		return redirect('/userprofile/')
	return render_to_response('user/edit_profile.html', {
			'form': form
		}, context_instance=RequestContext(request))
