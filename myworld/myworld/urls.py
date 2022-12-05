from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('blogs/', include('blogs.urls')),
    path('admin/', admin.site.urls),
] 