from django.shortcuts import render
from post.models import Post, Category
from post.forms import PostForm
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def view_post(request, post_id):
    category = Category.objects.all()
    post_category = None
    try :
        post = Post.objects.get(pk=post_id)
        #print("thumbnail", post.thumbnail.url)
        post_category = list(Post.objects.filter(pk=post_id).values("category__category_name"))
        post_category = [d['category__category_name'] for d in post_category]
        post_tags = post.tags.replace(post.title, '').split(' ')
    except Post.DoesNotExist:
        return render(request, "post/post_not_found.html", {"categories":category})
    return render(request, "post/post.html", {"post":post, "categories":category, 
                                              "post_categories":post_category,
                                              "post_tags":post_tags})

def post_list(request, category_name=None):
    posts= None
    category = Category.objects.all()
    if category_name:
        posts = Post.objects.filter(category__category_name=category_name).order_by('-created_on', 'pk')
        posts_exist = True
        paginator = Paginator(posts, 5)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        if not posts:
            posts_exist = False
        return render(request, 'post/post_list.html',
                         {"posts":posts, "category_name":category_name,
                          "categories":category, "posts_exist":posts_exist, "search_results": False})
    else:
        posts = Post.objects.all().order_by('-created_on', 'pk')
        paginator = Paginator(posts, 5)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request, 'post/post_list.html', {"posts":posts, 
                                                       "categories":category,
                                                       "search_results": False})

    
def search(request):
    category = Category.objects.all() 
    keywords = request.GET.get("keywords")
    #keywords = keywords.split(' ')
    #print(keywords)
    posts = Post.objects.filter(Q(title__icontains=keywords) | 
                                Q(description__icontains=keywords) |
                                Q(tags__icontains=keywords) |
                                Q(category__category_name__icontains=keywords)
                                ).order_by('-created_on', 'pk')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print("Searched once")
    return render(request, 'post/post_list.html', {"posts":posts, "categories":category,
                                                   "search_results": True, "keywords":keywords})

