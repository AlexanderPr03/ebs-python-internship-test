from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    enabled = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
 #   comments = models.ForeignKey(Comment, on_delete=models.CASCADE)

class Comment(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    