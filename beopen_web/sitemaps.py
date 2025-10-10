from django.contrib.sitemaps import Sitemap
from .models import Post
from django.urls import reverse

class PostMap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.modified_time

    def location(self, obj):
        return reverse('post', kwargs={'name': obj.post_name})

class OtherMap(Sitemap):
    priority = 1
    changefreq = 'weekly'

    def items(self):
        return ['index',]

    def location(self, item):
        return reverse(item)