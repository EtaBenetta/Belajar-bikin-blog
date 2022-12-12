from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('author/<int:id>', views.author, name='index'),
]
