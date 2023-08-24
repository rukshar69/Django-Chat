# Run redis server:  docker run --rm -p 6379:6379 redis:7

import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

from channels.routing import ProtocolTypeRouter, URLRouter

import room.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(room.routing.websocket_urlpatterns))
        )
})
