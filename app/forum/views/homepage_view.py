from django.views.generic import ListView, View
from django.shortcuts import render


def homepage(request):
    return render(request, 'forum/homepage.html', {})
    # return render(request, 'base.html', {})

# class HomePageView(View):
#     template_name = 'homepage'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
