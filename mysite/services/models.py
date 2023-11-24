from django.db import models

from django.db import models
from django.shortcuts import render
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.models import Page 
from wagtail.admin.panels import FieldPanel, InlinePanel
from taggit.models import Tag as TaggitTag, TaggedItemBase
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from wagtail.fields import StreamField, RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks
from .blocks import FirstServiceBlock, SecondServiceBlock, BodyBlock


class ServiceBlogPage(RoutablePageMixin, Page):
    description = RichTextField(max_length=60, help_text='Each sentence should have a max of 19 characters')
    displayed = StreamField([
        ('firsts', FirstServiceBlock()),
        ('secs', SecondServiceBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel('displayed'),
    ]

    # Define a method to get the context for rendering the blog page
    def get_context(self, request, *args, **kwargs):
        context = super(ServiceBlogPage, self).get_context(request, *args, **kwargs)
        # Add the blog page and the posts to the context
        context['service_blog_page'] = self
        context['posts'] = self.posts
        return context
    
    # Define a method to get the posts that are descendants of the blog page
    def get_posts(self):
        return ServicePostPage.objects.descendant_of(self).live()
    
    # Define a route for the blog page that shows the list of posts
    @route(r'^$')
    def post_list(self, request, *args, **kwargs):
        # Assign the posts to a variable
        self.posts = self.get_posts()
        return self.render(request)
    
    # Define another method to get the context for rendering the blog page
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['service_blog_page'] = self
        context['posts'] = self.posts
        return context
    
class ServicePostPage(Page):
    header_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL , related_name="+")
    body = StreamField([
        ('body_class',BodyBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("header_image"),
        FieldPanel('body'),
    ]
