from rest_framework import serializers
from forum.models import Topic
from django.contrib.auth.models import User


class TopicSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    date_posted = serializers.DateTimeField()
    author = serializers.CharField()

    class Meta:
        model = Topic
        fields = ['__all__']

    def create(self, validated_data):
        topic = Topic.objects.create(
            title=validated_data.get('title'),
            content=validated_data.get('content'),
            date_posted=validated_data.get('date_posted'),
            author=User.objects.get(username=validated_data.get('author'))
        )
        return topic
