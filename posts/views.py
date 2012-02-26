from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.http import Http404
from datetime import date

from information.models import *
from posts.models import *
from posts.forms import *

# Home page
def index(request):
	if request.user.id:
		try:
			up = UserProfile.objects.get(user=request.user.id)
		except UserProfile.DoesNotExist:
			return edit_profile(request)
	latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
	return render_to_response('posts/index.html', {
		'latest_post_list': latest_post_list,
		'is_at_home': True
	}, context_instance=RequestContext(request))

# Post detail
def detail(request, post_id):
	try:
		p = Post.objects.get(pk=post_id)
		l_user = l_post = ''
		if p.user.postcode:
			l_user = get_location_by_plz(p.user.postcode)
	except Post.DoesNotExist:
		raise Http404
	return render_to_response('posts/detail.html', {
			'post': p, 'where': p.location, 'place': l_user, 
			'replies': Reply.objects.filter(post=p), 
			'my_post': (p.user.user.id == request.user.id)
		}, context_instance=RequestContext(request))

# Add new post
def add(request):
	up = UserProfile.objects.get(user=request.user.id)
	form = PostForm(request.POST or None)
	if form.is_valid():
		post = form.save(commit=False)
		post.user_id = up.id
		post.save()
		messages.success(request, 'Thanks for posting!')
		return redirect('/posts/%d' % post.id)
	form.initial['postcode'] = up.postcode
	return render_to_response('posts/edit_post.html', {
			'form': form
		}, context_instance=RequestContext(request))
	
# Edut a post
def edit(request, post_id):
	up = UserProfile.objects.get(user=request.user.id)
	post = get_object_or_404(Post, id=post_id)
	form = PostForm(request.POST or None, instance=post)
	if form.is_valid():
		post = form.save(commit=False)
		post.user_id = up.id
		post.save()
		messages.success(request, 'Your post has been saved.')
		return redirect('/posts/%d' % post.id)
	return render_to_response('posts/edit_post.html', {
			'form': form, 'post': post
		}, context_instance=RequestContext(request))

# Replies to post
def reply(request, post_id, reply_id=-1):
	try:
		up = UserProfile.objects.get(user=request.user.id)
		p = Post.objects.get(pk=post_id)
		r = None
		if reply_id > -1:
			r = Reply.objects.get(pk=reply_id)
	except UserProfile.DoesNotExist:
		return edit_profile(request)
	form = ReplyForm(request.POST or None)
	if form.is_valid():
		reply = form.save(commit=False)
		reply.user_id = up.id
		reply.post_id = p.id
		if r != None:
			reply.reply_to = r
		reply.save()
		messages.success(request, 'Your message was sent.')
		return redirect('/posts/%d' % p.id)
	return render_to_response('posts/edit_reply.html', {
			'post': p, 'form': form
		}, context_instance=RequestContext(request))

# View my profile
def my_profile(request):
	try:
		up = UserProfile.objects.get(user=request.user.id)
		return profile(request, up.id)
	except UserProfile.DoesNotExist:
		return edit_profile(request)

# View my replies
def my_replies(request):
	try:
		up = UserProfile.objects.get(user=request.user.id)
		myposts = Post.objects.filter(user=up)
		replies = Reply.objects.filter(post__user=up)
		myreplies = Reply.objects.select_related().filter(user=up)
		replypostsdict = {}
		replyposts = []
		for r in myreplies:
			if not r.post.id in replypostsdict and r.post.user != up:
				replypostsdict[r.post.id] = True
				replyposts.append(r.post)
		return render_to_response('user/replies.html', {
				'userprofile': up,
				'myposts': myposts, 'replies': replies, 
				'replyposts': replyposts, 'myreplies': myreplies
			}, context_instance=RequestContext(request))
	except UserProfile.DoesNotExist:
		return edit_profile(request)

# View a profile		
def profile(request, userprofile_id):
	up = get_object_or_404(UserProfile, pk=userprofile_id)
	if up.postcode:
		user_location = get_location_by_plz(up.postcode)
	user_languages = ''
	user_age = ''
	if up.german:
		user_languages += 'German, '
	if up.french:
		user_languages += 'French, '
	if up.italian:
		user_languages += 'Italian, '
	if up.english:
		user_languages += 'English, '
	if up.other_lang:
		user_languages += up.other_lang
	elif user_languages != '':
		user_languages = user_languages[:-2]
	if up.birth_year:
		user_age = date.today().year - up.birth_year - 1
	return render_to_response('user/detail.html', {
			'userprofile': up, 'location': user_location,
			'languages': user_languages, 'age': user_age,
			'posts': Post.objects.filter(user=up), 
			'my_profile': (up.user.id == request.user.id)
		}, context_instance=RequestContext(request))

# View a user (via profile)
def user(request, user_id):
	up = get_object_or_404(UserProfile, user=user_id)
	return profile(request, up.id)

# Edit my profile
def edit_profile(request):
	newUser = False
	try:
		up = UserProfile.objects.get(user=request.user.id)
		form = UserProfileForm(request.POST or None, instance=up)
	except UserProfile.DoesNotExist:
		newUser = True
		form = UserProfileForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		user.user_id = request.user.id
		user.save()
		if newUser:
			messages.success(request, 'Your profile has been created, now check out what people like you have been posting:')
			return redirect('/')
		else:
			messages.success(request, 'Profile update saved.')
			return redirect('/userprofile/')
	return render_to_response('user/edit_profile.html', {
			'form': form
		}, context_instance=RequestContext(request))
