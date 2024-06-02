from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView

from forum.models import Topic


class DeleteTopicView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Topic
    success_url = '/'

    def test_func(self):
        topic = self.get_object()
        if self.request.user == topic.author:
            return True
        return False
