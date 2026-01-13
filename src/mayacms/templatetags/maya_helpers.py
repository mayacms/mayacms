from django import template
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site

register = template.Library()

# https://docs.djangoproject.com/en/6.0/ref/contrib/sites/
@register.filter
def site_url(uri, request=None):
    site = Site.objects.get_current()
    protocol = 'https' if request and request.is_secure() else 'http'
    host = request.get_host() if request else site.domain
    return '%s://%s%s' % (protocol, host, uri)

@register.simple_tag(takes_context=True, name='site_url')
def do_site_url(context, uri=''):
    """
    Generate full site URL with protocol detection using context request.
    """
    return site_url(uri, context.get('request'))

@register.simple_tag(takes_context=True, name='current_url')
def do_current_url(context):
    """
    Get the current full URL including query parameters.
    """
    request = context.get('request')
    if not request:
        return ''
    
    protocol = 'https' if request.is_secure() else 'http'
    host = request.get_host()
    path = request.get_full_path()  # Includes query string
    
    return '%s://%s%s' % (protocol, host, path)
