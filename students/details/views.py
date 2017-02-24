from django.shortcuts import render_to_response
import os
x = os.path.abspath(os.getcwd())

def index (request):
    return render_to_response(x + "/details/det.html")