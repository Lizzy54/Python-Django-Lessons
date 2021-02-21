from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField()
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'