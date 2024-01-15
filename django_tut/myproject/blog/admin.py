from django.contrib import admin
from .models import Article,Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'parent', 'position')
    list_filter = ('status',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = 'منتشر شد'
    else:
        message_bit = 'منشتر شدند'
    modeladmin.message_user(request, '{} مقاله {}'.format(rows_updated, message_bit))


make_published.short_discriotion = 'انتشار مقالات انتخاب شده'


def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = 'پیش نویس شد'
    else:
        message_bit = 'پیش نویس شدند'
    modeladmin.message_user(request, '{} مقاله {}'.format(rows_updated, message_bit))


make_published.short_discriotion = 'پیش نویس مقالات انتخاب شده'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag', 'slug', 'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-publish', 'status']
    actions = [make_published, make_draft]

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category_published()])

    category_to_str.short_description = 'دسته بندی'


admin.site.register(Article, ArticleAdmin)

