from django.db import models

class Article(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    text = models.TextField(verbose_name='Текст')
    date = models.DateField(verbose_name='Дата')
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField()
    article_id = models.IntegerField()
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'