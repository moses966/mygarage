from django import template
from home.models import IndexPage

register = template.Library()


@register.simple_tag
def display_index_images(name):
    index_page = IndexPage.objects.live().first()
    
    # Find the image with the specified title.
    image = index_page.gallery_image.filter(name=name).first()
    
    return image

@register.simple_tag
def display_mtn():
    index_page = IndexPage.objects.first()
    if index_page:
        return index_page.mtn_contact
    return ""

@register.simple_tag
def display_airtel():
    index_page = IndexPage.objects.first()
    if index_page:
        return index_page.airtel_contact
    return ""