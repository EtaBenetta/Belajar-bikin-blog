from django.db import models
from datetime import date


class Authors(models.Model):
  name = models.CharField(max_length=255)
  bio = models.CharField(max_length=255)
  twitter = models.CharField(max_length=255)
  facebook = models.CharField(max_length=255)
  instagram = models.CharField(max_length=255)
  image = models.ImageField(upload_to='media/images/')
  def __str__(self):
    return self.name


class Categories(models.Model):
  name = models.CharField(max_length=255)
  
  def __str__(self):
    return self.name

  def get_blog_count(self):
    print("test")
    #return Blogs.objects.filter(category = self.id).count()
    return 10



class Blogs(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  image = models.ImageField(upload_to='media/images/')
  writer_name = models.CharField(max_length=255)
  date = models.DateField(default=date.today)
  min_to_read = models.IntegerField()
  category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=None)
  author = models.ForeignKey(Authors, on_delete=models.CASCADE, default=None)
  def __str__(self):
    return self.title


