from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from beopen_web.models import Post
import os

class BeopenFeed(Feed):
    feed_type = Atom1Feed

    title = os.environ.get("SITE_TITLE")
    link = '/feed.xml'

    def items(self):
        return Post.objects.order_by("-create_time")[:10]

    def item_title(self, item):
        return item.post_title

    def item_link(self, item):
        return f"/posts/{item.post_name}/"

    def item_pubdate(self, item):
        return item.create_time

    def item_updateddate(self, item):
        return item.modified_time
