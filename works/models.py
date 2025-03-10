from django.db import models
from tags.models import  Tag

# Create your models here.

class Work(models.Model):
    title = models.CharField(max_length=255)
    # description = RichTextField()
    tags = models.ManyToManyField('tags.Tag',related_name='Works')
    image = models.ImageField(upload_to='works/',blank=True)    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        return self.title