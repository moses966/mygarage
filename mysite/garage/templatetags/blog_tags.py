from django import template
from garage.models import BlogPage

register = template.Library()


@register.simple_tag
def display_blog_images(name):
    blog_page = BlogPage.objects.live().first()
    
    # Find the image with the specified title.
    image = blog_page.gallery_images.filter(name=name).first()
    
    return image