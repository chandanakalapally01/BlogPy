from django.shortcuts import render

from .models import Post

# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, "blog/index.html", {"latest_posts": latest_posts})

def posts(request):
    posts = Post.objects.all().order_by("-date")
    print(posts)
    return render(request, "blog/posts.html", {"posts": posts})

def post_details(request, slug):
    post = Post.objects.get(slug = slug)
    tags = post.tags.all()
    return render(request, "blog/detailed-post.html",{"post": post, "tags":tags})
