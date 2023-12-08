from django.http import HttpResponse
from django.template import loader
from .models import Post
from .models import User
from .models import Comment
from .models import Category

def posts(request):
    allPost = Post.objects.all().values()
    template = loader.get_template('blogs.html')
    context = {
        'allPost': allPost,
    }
    return HttpResponse(template.render(context, request))

def blogdetails(request,id):
    detail = Post.objects.get(ID=id)
    template = loader.get_template('blogdetails.html')
    context = {
        'detail': detail,
    }
    return HttpResponse(template.render(context, request))

def users(request):
    allUsers = User.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'allUsers': allUsers,
    }
    return HttpResponse(template.render(context, request))

def comments(request):
    allComments = Comment.objects.all().values()
    template = loader.get_template('comments.html')
    context = {
        'allComments': allComments,
    }
    return HttpResponse(template.render(context, request))

def categories(request):
    allCategory = Category.objects.all().values()
    template = loader.get_template('categories.html')
    context = {
        'allCategory': allCategory,
    }
    return HttpResponse(template.render(context, request))

def postDetails(request, id):
  post = Post.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'post': post,
  }
  return HttpResponse(template.render(context, request))
def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
