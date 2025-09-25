from django.shortcuts import render
from django.http import HttpResponse
import os
# from dotenv import load_dotenv

def index(request):
    site_title = os.environ.get("SITE_TITLE")
    contex = {"site_title": site_title}
    return render(request, "index.html", contex)