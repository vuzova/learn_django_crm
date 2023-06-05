from django.db import models

# Create your models here.
class Articles(models.Model):
    create_date = models.DateField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Текст статьи')

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'


