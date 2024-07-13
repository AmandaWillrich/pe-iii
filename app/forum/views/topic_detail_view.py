from forum.models import Topic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib import messages


class TopicDetailView(LoginRequiredMixin, DetailView):
    model = Topic
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(
                self.request,
                messages.WARNING,
                'Para acessar o tópico, é necessário estar logado.'
            )
        return super().dispatch(request, *args, **kwargs)