from django.shortcuts import render

# Create your views here.
def newpost(request):
    return render(request, "newpost/newpost.html")