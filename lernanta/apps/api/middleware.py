from django.http import HttpResponsePermanentRedirect, Http404, HttpResponse
from django.conf import settings


class APISubdomainMiddleware:
    def process_request(self, request):
        #"""Parse out the subdomain from the request and redirect to API"""
        #host = request.META.get('HTTP_HOST', '')
        #host_s = host.replace('www.', '').split('.')
        #if (host_s[0] == 'api'):
        #  return HttpResponsePermanentRedirect('http://' + host_s[1] + '.' + host_s[2]
        #      + '/api' + request.path + '?' + request.GET.urlencode(safe='&'))

        # Check if API_DOMAIN is True.
        # The URLCONF_ROOT will be replaced and only the api urls will be available.
        if settings.API_DOMAIN:
            request.urlconf = 'lernanta.apps.api.urls'
        else:
            raise Http404
            
        return None

