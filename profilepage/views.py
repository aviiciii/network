from django.shortcuts import render, redirect
from network.models import User
from django.core.paginator import Paginator

# Create your views here.
def profile(request, username):
    # Get the user object
    profile = User.objects.get(username=username)
    # Get number of followers and following
    followers = profile.followers.all()
    following = profile.following.all()

    # Get the user's posts
    posts = profile.posts.all().order_by('-timestamp')

    # Paginate the posts
    paginator = Paginator(posts, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_pages = range(1, paginator.num_pages+1)

    # check if user is a follower
    if request.user in followers:
        is_follower = True
    else:
        is_follower = False

    # Pass the user and posts to the template
    context={'profile': profile, 'followers': followers, 'following': following, 'page_obj': page_obj, 'total_pages': total_pages, 'is_follower': is_follower}


    return render(request, "profilepage/profile.html", context=context)

def follow(request, username):
    # get user
    profile = User.objects.get(username=username)

    # get curent user
    current_user = request.user

    # get current user's following
    current_user.following.add(profile)
    profile.followers.add(current_user)
    
    return redirect("profile", username=username)

def unfollow(request, username):
    
    # get user
    profile = User.objects.get(username=username)

    # get curent user
    current_user = request.user

    # get current user's following
    current_user.following.remove(profile)
    profile.followers.remove(current_user)

    return redirect("profile", username=username)

