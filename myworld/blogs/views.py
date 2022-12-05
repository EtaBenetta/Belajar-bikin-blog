from django.http import HttpResponse
from django.template import loader

from .models import Blogs

def index(request):
  template = loader.get_template('index.html')
  myblogs = Blogs.objects.all().values()

  context = {
    'myblogs': myblogs,
  }

  return HttpResponse(template.render(context, request))
  