from django.shortcuts import render
from django.views import View
import markdown
from beopen_web.models import Post
from django.conf import settings
import os
from django.db.models import F
from django.http import HttpResponseNotFound

class PostView(View):

    def get(self, request, name):

        base_dir = settings.BASE_DIR

        post_file_dir = os.path.abspath(os.path.join(base_dir, "..", os.environ.get("POST_FILE_DIR")))

        post_record = Post.objects.filter(post_name = name)
        post = post_record.first()

        if post == None:
            return HttpResponseNotFound("页面不存在")

        with open(os.path.join(post_file_dir, post.content_file_path), "r", encoding="utf-8") as f:
            md_content = f.read()

        html_content = markdown.markdown(md_content)

        post_record.update(visit_count = F("visit_count") + 1)

        return render(request, "post.html", {"content": html_content, "post": post})
