from django.shortcuts import render
from django.core.paginator import Paginator
from .models import BlogPost


def blog_post_list(request):
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(blog_posts, 2)  # 9 posts per page (3 columns * 3 rows)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog-list.html', {'page_obj': page_obj})



def single_post(request, id):
    blog_post = BlogPost.objects.filter(id=id).first()
    print(blog_post)
    return render(request, 'single-post.html', {'blog_post': blog_post})