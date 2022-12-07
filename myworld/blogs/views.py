from django.http import HttpResponse
from django.template import loader

from .models import Authors, Blogs

def index(request):
  template = loader.get_template('index.html')
  myblogs = Blogs.objects.all().values()
  myauthors = Authors.objects.all().values()


  context = {
    'myblogs': myblogs,
    'myauthors' : myauthors,
  }

  return HttpResponse(template.render(context, request))
  