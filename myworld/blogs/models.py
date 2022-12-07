from django.db import models
from datetime import date

class Blogs(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  image = models.ImageField()
  writer_name = models.CharField(max_length=255)
  date = models.DateField(default=date.today)
  min_to_read = models.IntegerField()
  def __str__(self):
    return self.title

class Authors(models.Model):
  name = models.CharField(max_length=255)
  bio = models.CharField(max_length=255)
  twitter = models.CharField(max_length=255)
  facebook = models.CharField(max_length=255)
  instagram = models.CharField(max_length=255)
  image = models.ImageField()
  def __str__(self):
    return self.name