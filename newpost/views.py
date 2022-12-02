from django.shortcuts import render
from network.models import User, Post
from project4.settings import LOGIN_REDIRECT_URL
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url=LOGIN_REDIRECT_URL)
def newpost(request):
    if request.method == 'POST':
        post = request.POST['post']
        user = request.user
        new_post = Post(user=user, content=post)
        new_post.save()
        return render(request, 'network/index.html')
        
    return render(request, "newpost/newpost.html")