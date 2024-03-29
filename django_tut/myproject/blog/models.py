from django.db import models
from django.utils import timezone
from extenstions.utils import jalali_convertor
from django.utils.html import format_html
from django.contrib.auth.models import User


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='children', verbose_name='زیردسته بندی')
    title = models.CharField(max_length=100,verbose_name='عنوان')
    slug = models.SlugField(verbose_name='اسلاگ')
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')
    position = models.IntegerField(verbose_name='پوزیشین')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title
    objects = CategoryManager()


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'published')
    )
    title = models.CharField(max_length=200,  verbose_name ='عنوان')
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,
                               related_name='articles', verbose_name='نویسنده')
    slug = models.SlugField(max_length=100, unique=True,  verbose_name='اسلاگ')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='articles')
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

    def jpublish(self):
        return jalali_convertor(self.publish)
    jpublish.short_description = 'تاریخ انتشار'

    def category_published(self):
        return self.category.filter(status=True)

    def thumbnail_tag(self):
        return format_html('<img src={} width=100 height=75>'.format(self.thumbnail.url))
    thumbnail_tag.short_discription = 'تصویر'


    objects = ArticleManager()



