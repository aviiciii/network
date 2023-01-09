from django.shortcuts import render
from network.models import User, Post
from project4.settings import LOGIN_REDIRECT_URL
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
@login_required(login_url=LOGIN_REDIRECT_URL)
def newpost(request):
    if request.method == 'POST':
        post = request.POST['post']
        user = request.user
        new_post = Post(user=user, content=post.strip())
        new_post.save()
        return redirect('index')
        
    return render(request, "newpost/newpost.html")