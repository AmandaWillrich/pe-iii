from django.urls import include, path
from rest_framework import routers

from .views import topic_view, users_view

router = routers.DefaultRouter()
router.register(r'users', users_view.UserViewSet)
router.register(r'topic', topic_view.TopicView)


urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]