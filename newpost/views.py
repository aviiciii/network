from django.shortcuts import render

# Create your views here.
def newpost(request):
    if request.method == 'POST':
        post = request.POST['post']
        print(post)
    return render(request, "newpost/newpost.html")