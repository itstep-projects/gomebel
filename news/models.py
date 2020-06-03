from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    about = models.TextField(max_length=256, null=False)
    text = models.TextField(null=False)
    author = models.CharField(max_length=100, null=False)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    image = models.FileField(null=False, upload_to='upload/')
    published = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    comment = models.TextField(null=False)
    date = models.DateTimeField(null=False, default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post} / {self.name}'
