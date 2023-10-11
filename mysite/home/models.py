from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel


class HomePage(Page):
    pass


class IndexPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        InlinePanel('gallery_image', label="Gallery images"),
    ]

class HomeGalleryImage(Orderable):
    page = ParentalKey(IndexPage, on_delete=models.CASCADE, related_name='gallery_image')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)
    name = models.CharField(blank=True, max_length=50)
    

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
        FieldPanel('name'),
    ]
