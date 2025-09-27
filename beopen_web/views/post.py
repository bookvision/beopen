from django.shortcuts import render
from django.views import View
import markdown
from beopen_web.models import Post
from django.conf import settings
import os

class PostView(View):

    def get(self, request, name):

        base_dir = settings.BASE_DIR

        post_file_dir = os.path.abspath(os.path.join(base_dir, "..", os.environ.get("POST_FILE_DIR")))

        post = Post.objects.filter(post_name = name).first()
        with open(os.path.join(post_file_dir, post.content_file_path), "r", encoding="utf-8") as f:
            md_content = f.read()

        html_content = markdown.markdown(md_content)

        return render(request, "post.html", {"content": html_content, "post": post})
