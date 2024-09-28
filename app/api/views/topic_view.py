from forum.models import Topic
from rest_framework import viewsets

from api.serializers.topic_serializer import TopicSerializer
from rest_framework import viewsets


class TopicView(viewsets.ModelViewSet):
    """
    API endpoint that allows topics to be viewed or edited.
    """
    queryset = Topic.objects.all().order_by('-date_posted')
    serializer_class = TopicSerializer
    # permission_classes = [permissions.IsAuthenticated]
