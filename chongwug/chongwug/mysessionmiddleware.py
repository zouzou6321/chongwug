from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from django.utils.importlib import import_module
class mySessionMiddleware(SessionMiddleware):
    def process_request(self, request):
        engine = import_module(settings.SESSION_ENGINE)
        session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME, None)
        if not session_key:
            if 'sessionid' in request.POST:
                session_key = request.POST['sessionid']
                print request.POST['sessionid']
        request.session = engine.SessionStore(session_key)