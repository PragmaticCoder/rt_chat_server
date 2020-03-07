import json

from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        self.room_name = 'chatter'  # single thread id.
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        print(event)

        await self.send({"type": "websocket.accept"})
        await self.send({"type": "websocket.send"})

    async def websocket_receive(self, event):
        print(f'websocket_receiver: {event}')

        message_data = json.loads(event['text'])
        user = self.scope['user']

        if user.is_authenticated:
            username = user.username
            message_data['username'] = username

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': json.dumps(message_data)
                }
            )

    async def chat_message(self, event):
        print(event)
        message_data = json.loads(event['message'])

        await self.send({
            "type": "websocket.send",
            "text": json.dumps(message_data)
        })

    async def websocket_disconnect(self, event):
        print(event)
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    @database_sync_to_async
    def get_name(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return 'Unknown User'

        return f'{user.first_name} {user.last_name}'
