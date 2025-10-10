from django.urls import path
from .views.main import MainView
from .views.post import PostView
from .views.feed import BeopenFeed
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostMap, OtherMap
from django.http import HttpResponse
import os

sitemaps_dict = {
    'articles': PostMap,
    'other': OtherMap,
}

from django.urls import path

def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow:",
        "Allow: /",
        "Sitemap: %s/sitemap.xml" % (os.environ.get("SITE_FULL_URL", "")),
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

urlpatterns = [
    path('', MainView.as_view(), name="index"),
    path('post/<str:name>', PostView.as_view(), name="post"),
    path("feed.xml", BeopenFeed(), name="atom_feed"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps_dict}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", robots_txt, name="robots_txt"),
]
