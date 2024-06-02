from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from forum.models import Topic


class CreateTopicView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
