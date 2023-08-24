from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    #path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]