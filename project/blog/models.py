from django.db import models

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='blog-images', null=True, blank=True, )
    thumbsup = models.IntegerField(default=0, )
    thumbsdn = models.IntegerField(default=0, )


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True, )
    author = models.TextField()
    comment = models.TextField()
    thumbsup = models.IntegerField(default=0, )
    thumbsdn = models.IntegerField(default=0, )
    visible = models.BooleanField(default=False, )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
