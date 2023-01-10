from django.shortcuts import render
from network.models import Post, User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from project4.settings import LOGIN_REDIRECT_URL


# Create your views here.
@login_required(login_url=LOGIN_REDIRECT_URL)
def following_feed(request):
    # get current users following
    user = request.user
    following= user.following.all()
    
    # posts of people the user is following
    posts= Post.objects.filter(user__in= following).order_by('-timestamp')

    # paginate
    paginator = Paginator(posts, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_pages = range(1, paginator.num_pages+1)



    return render(request, 'followingfeed/followingfeed.html', {'page_obj': page_obj, 'total_pages': total_pages})