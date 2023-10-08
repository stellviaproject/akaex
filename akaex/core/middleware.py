import threading
import http.client
import email.parser

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class ModelRequestMiddleware(MiddlewareMixin):
    """
    Provides storage for the "current" request object, so that code anywhere
    in your project can access it, without it having to be passed to that code
    from the view.
    """
    _requests = {}

    def process_request(self, request):
        """
        Store the current request.
        """
        self.__class__.set_request(request)

    def process_response(self, request, response):
        """
        Delete the current request to avoid leaking memory.
        """
        self.__class__.del_request()
        return response

    @classmethod
    def get_request(cls, default=None):
        """
        Retrieve the request object for the current thread, or the optionally
        provided default if there is no current request.
        """
        return cls._requests.get(threading.current_thread(), default)

    @classmethod
    def set_request(cls, request):
        """
        Save the given request into storage for the current thread.
        """
        cls._requests[threading.current_thread()] = request

    @classmethod
    def del_request(cls):
        """
        Delete the request that was stored for the current thread.
        """
        cls._requests.pop(threading.current_thread(), None)


class CacheControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if '/api/' in request.path:
            response['Cache-Control'] = 'no-cache, max-age=100'
        return response


# If settings.DEBUG is True disable CSRF protection.
# This will not work in production.
class DisableCSRFMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #if settings.DEBUG:
        setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        return response


class DisableHeaderLimitMiddleware(MiddlewareMixin):
    """
    Middleware to disable the limit of the header size
    """
    def __init__(self, get_response):
        self.get_response = get_response

        def parse_headers(fp, _class=http.client.HTTPMessage):
            headers = []
            while True:
                line = fp.readline(http.client._MAXLINE + 1)
                headers.append(line)
                if line in (b'\r\n', b'\n', b''):
                    break
            hstring = b''.join(headers).decode('iso-8859-1')
            return email.parser.Parser(_class=_class).parsestr(hstring)

        http.client.parse_headers = parse_headers


class CoreRequestMiddleware(MiddlewareMixin):
    """
    Provides storage for the "current" request object, so that code anywhere
    in your project can access it, without it having to be passed to that code
    from the view.
    """
    _requests = {}

    def process_request(self, request):
        """
        Store the current request.
        """
        self.__class__.set_request(request)

    def process_response(self, request, response):
        """
        Delete the current request to avoid leaking memory.
        """
        self.__class__.del_request()
        return response

    @classmethod
    def get_request(cls, default=None):
        """
        Retrieve the request object for the current thread, or the optionally
        provided default if there is no current request.
        """
        return cls._requests.get(threading.current_thread(), default)

    @classmethod
    def set_request(cls, request):
        """
        Save the given request into storage for the current thread.
        """
        cls._requests[threading.current_thread()] = request

    @classmethod
    def del_request(cls):
        """
        Delete the request that was stored for the current thread.
        """
        cls._requests.pop(threading.current_thread(), None)