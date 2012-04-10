from django.contrib.sites.models import Site
from django.http import HttpResponse


class LernantaResourceMiddleware(object):
	
	def process_request(self, request):
		"""
		Check if the requested resource is available to serve.
		"""
		return None
