from django.shortcuts import render
from django.views import View
from beopen_web.models import Post
import os

class MainView(View):

    def get(self, request):

        post_list = Post.objects.all().order_by("-create_time")
        contex = {"post_list": post_list}

        return render(request, "index.html", contex)