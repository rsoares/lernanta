from django.http import HttpResponsePermanentRedirect, Http404, HttpResponse
from django.conf import settings
from lernanta.apps.api import urls

class APISubdomainMiddleware:
    def process_request(self, request):
        # Check if API_DOMAIN is on
        if settings.API_DOMAIN:
            #raise Http404  #  Should I raise Http404?
            request.urlconf = urls.urlpatterns

        """Parse out the subdomain from the request and redirect to API"""
        host = request.META.get('HTTP_HOST', '')
        host_s = host.replace('www.', '').split('.')
        if (host_s[0] == 'api'):
          return HttpResponsePermanentRedirect('http://' + host_s[1] + '.' + host_s[2]
              + '/api' + request.path + '?' + request.GET.urlencode(safe='&'))

