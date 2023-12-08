from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Name


class Post(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Date_Published = models.DateField()
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.Title


class Comment(models.Model):
    ID = models.AutoField(primary_key=True)
    Post_ID = models.ForeignKey(Post, on_delete=models.CASCADE)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Date_Posted = models.DateField(auto_now_add=True)
    Content = models.TextField()

    def __str__(self):
        return self.Content
