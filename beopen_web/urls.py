from django.urls import path
from .views.main import MainView
from .views.post import PostView
from .views.feed import BeopenFeed

urlpatterns = [
    path('', MainView.as_view(), name="index"),
    path('post/<str:name>', PostView.as_view(), name="post"),
    path("feed.xml", BeopenFeed(), name="atom_feed"),
]
