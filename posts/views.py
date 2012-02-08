from django.shortcuts import render_to_response
from django.http import Http404
from posts.models import Post

def index(request):
	latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
	return render_to_response('posts/index.html', {
		'latest_post_list': latest_post_list,
	})
	
def detail(request, post_id):
	try:
		p = Post.objects.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404
	return render_to_response('posts/detail.html', {
			'post': p,
		})