from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Page, Post

from .forms import PageForm, PostForm

# Create your views here.
def index(request):
    return render(request, 'blogs/index.html')

def pages(request):
    pages = Page.objects.order_by('date_added')
    context = {'pages': pages}
    return render(request, 'blogs/pages.html', context)

def page(request, page_id):
    page = Page.objects.get(id=page_id)
    posts = page.post_set.order_by('-date_added')
    context = {'page': page, 'posts': posts}
    return render(request, 'blogs/page.html', context)

@login_required
def new_page(request):
    check_topic_owner(request, page)
    if request.method != 'POST':
        form = PageForm()
    else:
        form = PageForm(data=request.POST)
        if form.is_valid():
            new_page = form.save(commit = False)
            new_page.owner = request.user
            new_page.save()
            return redirect('blogs:pages')

    context = {'form': form}
    return render(request, 'blogs/new_page.html', context)

@login_required
def new_post(request, page_id):
    page = Page.objects.get(id=page_id)
    check_topic_owner(request, page)

    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.page = page
            new_post.save()
            return redirect('blogs:page', page_id=page_id)

    context = {'page': page, 'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    page = post.page
    check_topic_owner(request, page)
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:page', page_id=page.id)

    context = {'post': post, 'page': page, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

def check_topic_owner(request, page):
    if page.owner != request.user:
        raise Http404