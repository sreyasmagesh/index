from django.shortcuts import render

def index(req):
    return render(req,'new.html')
