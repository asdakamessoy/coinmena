import json

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from coinmena.settings import CLIENT_API_KEY


API_KEY = "api_key"


class HttpResponseForbidden(HttpResponse):
    status_code = 403


class ApiCallMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = None
        if hasattr(self, "process_request"):
            response = self.process_request(request)

        if not response:
            response = self.get_response(request)

        if hasattr(self, "process_response"):
            response = self.process_response(request, response)
        return response

    def process_view(self, request, view_func, args, kwargs):
        if request.GET.get(API_KEY) != CLIENT_API_KEY:
            return HttpResponseForbidden()
        if request.method == "POST":
            try:
                # TODO: - we may be able to drop this in python 3.7 - needed for python 3.5
                request.json = json.loads(request.body.decode("utf-8"))
            except ValueError:
                # Not a json body.
                request.json = {}
