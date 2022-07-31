from pickle import GET
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, CreateView

from .models import Post
from .forms import PostForm

# Create your views here.
class post_list(CreateView):
    template_name = "blog/post_list.html"
    model = Post
    fields = ["author", "title", "text", "created_date", "published_date"]

    def get(self, request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
            "published_date"
        )
        return render(request, "blog/post_list.html", {"posts": posts})


class post_detail(CreateView):
    # template_name = 'post_detail.html'
    model = Post
    fields = ["author", "title", "text", "created_date", "published_date"]

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, "blog/post_detail.html", {"post": post})


class post_new(CreateView):
    form_class = Post
    template_name = 'blog/post_edit.html'
    
    def get(self, request):
        form = PostForm()
        return render(request, "blog/post_edit.html", {"form": form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)


class post_edit(CreateView):
    form_class = Post
    template_name = 'blog/post_edit.html'

    
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        return render(request, "blog/post_edit.html", {"form": form})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
