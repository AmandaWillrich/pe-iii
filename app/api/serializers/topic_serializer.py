from rest_framework import serializers
from forum.models import Topic
from django.contrib.auth.models import User

class TopicSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username')  # Use the author's username

    class Meta:
        model = Topic
        fields = ['id', 'title', 'content', 'date_posted', 'author']

    def create(self, validated_data):
        author_username = validated_data.pop('author')['username']
        author = User.objects.get(username=author_username)
        topic = Topic.objects.create(
            author=author,
            **validated_data
        )
        return topic
