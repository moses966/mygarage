from django import template
from home.models import IndexPage

register = template.Library()


@register.simple_tag
def display_index_images(name):
    index_page = IndexPage.objects.live().first()
    
    # Find the image with the specified title.
    image = index_page.gallery_image.filter(name=name).first()
    
    return image