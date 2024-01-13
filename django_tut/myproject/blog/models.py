from django.db import models
from django.utils import timezone


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'published')
    )
    title = models.CharField(max_length=200,  verbose_name ='عنوان')
    slug = models.SlugField(max_length=100, unique=True,  verbose_name = 'اسلاگ')
    description = models.TextField(verbose_name='بدنه')
    thumbnail = models.ImageField(upload_to='images',  verbose_name ='تصویر')
    publish = models.DateTimeField(default=timezone.now(),  verbose_name ='انتشار')
    created = models.DateTimeField(auto_now_add=True,  verbose_name ='ساخته شده در ')
    updated = models.DateTimeField(auto_now=True,  verbose_name ='بروزرسانی شده در')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,  verbose_name ='وضعیت')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title


