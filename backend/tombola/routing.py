from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import re_path
from game.consumers import GameConsumer

websocket_urlpatterns = [
    re_path(r'ws/game/(?P<game_id>\w+)/$', GameConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
}) 