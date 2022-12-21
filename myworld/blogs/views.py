from django.http import HttpResponse
from django.template import loader

from .models import Authors, Blogs, Categories

def index(request):
  template = loader.get_template('index.html')
  myblogs = Blogs.objects.all()
  myauthors = Authors.objects.all().values()
  categories = Categories.objects.all().values()


  context = {
    'myblogs': myblogs,
    'myauthors' : myauthors,
    'categories' : categories,
  }

  return HttpResponse(template.render(context, request))

def author(request, id):
  myauthor = Authors.objects.get(id=id)
  template = loader.get_template('about-author.html')
  context = {
    'myauthor': myauthor,
  }
  return HttpResponse(template.render(context, request))


def about(request):
  template = loader.get_template('about_us.html')
  context = {

  }
  return HttpResponse(template.render(context, request))
