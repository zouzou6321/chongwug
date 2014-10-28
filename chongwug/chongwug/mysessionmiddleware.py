from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from django.utils.importlib import import_module
class mySessionMiddleware(SessionMiddleware):
    def process_request(self, request):
        engine = import_module(settings.SESSION_ENGINE)
        if 'sessionid' in request.POST:
            session_key = request.POST['sessionid']
        else:
            session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME, None)
        request.session = engine.SessionStore(session_key)