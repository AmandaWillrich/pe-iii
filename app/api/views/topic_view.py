from django.http import JsonResponse
from forum.models import Topic
from django.contrib.auth.models import User
from rest_framework import viewsets

from api.serializers import TopicSerializer


class TopicView(viewsets.ModelViewSet):
    """
    API endpoint that allows topics to be viewed or edited.
    """
    queryset = Topic.objects.all().order_by('-date_posted')
    serializer_class = TopicSerializer
    # permission_classes = [permissions.IsAuthenticated]
