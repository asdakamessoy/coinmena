import functools

from django.http import HttpResponseNotFound


def method_restricted(func, method_types, msg=None):
    if method_types and not isinstance(method_types, list):
        method_types = [method_types]

    @functools.wraps(func)
    def wrapped_function(request, *args, **kwargs):
        if method_types and request.method not in method_types:
            return HttpResponseNotFound()
        return func(request, *args, **kwargs)

    return wrapped_function


def post_only(func):
    return method_restricted(func, "POST")


def get_only(func):
    return method_restricted(func, "GET")
