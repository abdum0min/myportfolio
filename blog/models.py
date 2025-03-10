from django.db import models
# from ckeditor.fields import RichTextField
from tags.models import Tag

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    # content = RichTextField()
    tags = models.ManyToManyField('tags.Tag',related_name='Posts')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comment(models.Model):
    blog = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments' 