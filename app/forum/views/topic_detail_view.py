from forum.models import Topic
from django.views.generic import DetailView


class TopicDetailView(DetailView):
    model = Topic
