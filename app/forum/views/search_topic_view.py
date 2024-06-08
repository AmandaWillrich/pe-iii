from django.views.generic import ListView
from forum.models import Topic


class SearchTopicView(ListView):
    model = Topic
    template_name = 'forum/homepage.html'
    context_object_name = 'topics'

    def get_queryset(self):
        result = super(SearchTopicView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Topic.objects.filter(title__contains=query)
            result = postresult
        else:
            result = None
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context
