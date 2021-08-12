from rest_framework import serializers
from datetime import datetime
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","blogproject.settings" )

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')
serializer = CommentSerializer(comment)
print(type(serializer.data))