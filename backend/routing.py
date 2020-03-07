from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.conf.urls import url

from backend.chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    # Websocket chat handler
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r'chat/', ChatConsumer, name='chat'),
                    # url(r'chat/(?P<username>[\w.@+-]+)', ChatConsumer, name='chat'),
                ]
            ),
        ),
    )
})
