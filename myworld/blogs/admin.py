from django.contrib import admin
from blogs.models import Blogs
from blogs.models import Authors
from blogs.models import Categories

admin.site.register(Blogs)
admin.site.register(Authors)
admin.site.register(Categories)



