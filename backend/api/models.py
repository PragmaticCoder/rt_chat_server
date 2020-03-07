from django.conf import settings
from django.db import models
from rest_framework import serializers

# from src.chat.managers import ThreadManager


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')


class Thread(models.Model):
    class Meta:
        db_table = 'chatxchannels_thread'
        verbose_name_plural = 'threads'

    # objects = ThreadManager()

    first = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chat_thread_first')
    second = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chat_thread_second')

    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'<Thread: {self.id}>'


class ChatMessage(models.Model):
    class Meta:
        db_table = 'chatxchannels_chat_message'
        verbose_name_plural = 'chat_messages'

    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='sender', on_delete=models.CASCADE)

    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'From: {self.user.username} -> {self.thread}'
