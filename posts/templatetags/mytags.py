import urllib, hashlib
from django import template

register = template.Library()

@register.inclusion_tag('templatetags/gravatar.html')
def show_gravatar(email, size=48):
    default = "http://0.gravatar.com/avatar/00e1dd94340133b9daf6e291fb766266"

    url = "http://www.gravatar.com/avatar.php?"
    url += urllib.urlencode({
        'gravatar_id': hashlib.md5(email).hexdigest(),
        #'default': default,
        'size': str(size)
    })

    return {'gravatar': {'url': url, 'size': size}}