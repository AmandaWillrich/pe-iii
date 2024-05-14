from django.urls import path
# from .views import HomePageView
from .views import homepage


urlpatterns = [
    # path('', HomePageView.as_view(), name='homepage')
    path('', homepage, name='homepage')
]
