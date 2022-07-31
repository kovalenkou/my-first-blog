from pickle import GET
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, CreateView

from blog.models import Post

# Create your views here.
class post_list(CreateView):
    template_name = 'blog/post_list.html'
    model = Post
    fields = ['author', 'title', 'text', 'created_date', 'published_date']
    
    def get(self, request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'blog/post_list.html', {'posts': posts} )

    def post(self, request):
      return HttpResponse('Class based view')

    
class post_detail(CreateView):
    # template_name = 'post_detail.html'
    model = Post
    fields = ['author', 'title', 'text', 'created_date', 'published_date']
    
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})
