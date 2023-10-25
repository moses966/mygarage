from django import template
from garage.models import BlogPage

# template library to register custom template tags
register = template.Library()


@register.simple_tag
def display_blog_images(name):
    # Retrieve the first live BlogPage instance.
    blog_page = BlogPage.objects.live().first()
    
    # Find the image with the specified title.
    image = blog_page.gallery_images.filter(name=name).first()
    # Return the found image, which can be displayed in the template.
    return image