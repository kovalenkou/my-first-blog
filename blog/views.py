from pickle import GET
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from django.views.generic import TemplateView, CreateView

from blog.models import Post

# Create your views here.
class post_list(CreateView):
    template_name = 'blog/post_list.html'
    model = Post
    fields = ['author', 'title']

    # def post_list(self, request):
    #     return render(request, 'blog/post_list.html', {})

    # def get(self, request):
    #    return HttpResponse('Class based view')

    # def post(self, request):
    #   return HttpResponse('Class based view')