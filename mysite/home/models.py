from django.db import models
from django.shortcuts import redirect

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.blocks import PageChooserBlock
from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
)

# HomePage model representing the root page of the website
class HomePage(Page):
    pass

# Index Page
class IndexPage(Page):
    body = RichTextField(blank=True)

    featured = StreamField([
        ('services', PageChooserBlock(required=False)),
        ('posts', PageChooserBlock(required=False)),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        InlinePanel('gallery_image', label="Gallery images"),
        FieldPanel('featured'),
    ]

    
# Orderable model
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

# page which handles the redirection from the root URL ('/') to '/home/'
# this is implemented at; path('', include(wagtail_urls))
class RootRedirectPage(Page):
    def serve(self, request):
        return redirect('/home/')