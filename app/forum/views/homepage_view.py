from django.views.generic import ListView
from forum.models import Topic

class HomePageView(ListView):
    model = Topic
    template_name = 'forum/homepage.html'
    context_object_name = 'topics'
    ordering = ['-date_posted']
    paginate_by = 10 ## verificar essa paginação

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
