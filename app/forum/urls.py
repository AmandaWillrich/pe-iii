from django.urls import path
from forum.views import (
    HomePageView,
    CreateTopicView,
    TopicDetailView,
    DeleteTopicView,
    UpdateTopicView,
    ContactView,
    SearchTopicView
)


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('topico/novo/', CreateTopicView.as_view(), name='create_topic'),
    path('topico/<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
    path('topico/<int:pk>/atualizar', UpdateTopicView.as_view(), name='update_topic'),
    path('topico/<int:pk>/deletar', DeleteTopicView.as_view(), name='delete_topic'),
    path('contato/', ContactView.as_view(), name='contact'),
    path('pesquisar/', SearchTopicView.as_view(), name='search_result'),
]
