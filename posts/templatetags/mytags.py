import urllib, hashlib
from django import template

register = template.Library()

# Renders a Gravatar based on the email, example usage:
# 	{% show_gravatar post.user.user.email 64 %}
#
@register.simple_tag
def show_gravatar(email, size=48):
	default = "http://0.gravatar.com/avatar/00e1dd94340133b9daf6e291fb766266"
	url = "http://www.gravatar.com/avatar.php?"
	url += urllib.urlencode({
		'gravatar_id': hashlib.md5(email).hexdigest(),
		#'default': default,
		'size': str(size)
	})
	result = '<img class="gravatar" src="%s" width="%s" border="0" />' % (url, size)
	return result

# Renders a fruity avatar from a profile ID
# 	{% show_fruvatar post.user.id 64 %}
#
@register.simple_tag
def show_fruvatar(profileid, size=48):
	url = "/static/images/fruitface.jpg"
	result = '<img class="fruvatar" src="%s" width="%s" border="0" />' % (url, size)
	result = '' # disable	
	return result

# Renders a post
#
@register.inclusion_tag('templatetags/post.html')
def show_post(post):
	return {'post': post}
