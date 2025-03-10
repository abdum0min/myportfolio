from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True)

    class Meta:
        ordering = ['name']
        verbose_name ='Tag'
        verbose_name_plural ='Tag'

    def __str__(self):
        return self.name