from django import template
from garage.models import Tag, BlogCategory

# template library to register custom template tags
register = template.Library()


@register.inclusion_tag('garage/components/categories_list.html',
                        takes_context=True)
def categories_list(context):
    categories = BlogCategory.objects.all()
    return {
        'request': context['request'],
        'blog_page': context['blog_page'],             
        'categories': categories
    }


@register.inclusion_tag('garage/components/tags_list.html',
                        takes_context=True)
def tags_list(context):
    tags = Tag.objects.all()
    return {
        'request': context['request'],
        'blog_page': context['blog_page'],              
        'tags': tags
    }
