from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.templatetags.static import static
from .models import Post, User



def index(request):
    posts = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(posts, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_pages = range(1, paginator.num_pages+1)

    return render(request, 'network/index.html', {'page_obj': page_obj, 'total_pages': total_pages})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def edit(request, post_id):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        edit_post=Post.objects.get(pk=post_id)
        edit_post.content= data["content"]
        edit_post.save()
        
        return JsonResponse({
            "message":"Change Successful",
            "data": data["content"]
        })

def like(request, post_id):
    if request.method == 'POST':

        data = json.loads(request.body)

        like_post = Post.objects.get(pk=post_id)
        
        if data["status"]=='unliked':
            like_post.likes.add(request.user)
            like_post.save()
            message='Liked successfully'
            likes = like_post.like_count()
            status= 'liked'
            print(likes)
            path=static('network/img/liked.png')

        elif data["status"]=='liked':
            like_post.likes.remove(request.user)
            like_post.save()
            message='Unliked successfully'
            path=static('network/img/unliked.png')
            likes = like_post.like_count()
            status= 'unliked'
            print(likes)
        else:
            print('some typo')

        return JsonResponse({
            "message":message,
            "path":path,
            "nooflikes":likes,
            "status": status
        })