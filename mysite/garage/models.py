from django.db import models
from django.shortcuts import render
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.models import Page
from wagtailmetadata.models import MetadataPageMixin
from wagtail.admin.panels import FieldPanel, InlinePanel
from taggit.models import Tag as TaggitTag, TaggedItemBase
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks





class BlogPage(RoutablePageMixin, Page):
    description = models.CharField(max_length=250, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]
    
    # Define a method to get the context for rendering the blog page
    def get_context(self, request, *args, **kwargs):
        context = super(BlogPage, self).get_context(request, *args, **kwargs)
        # Add the blog page and the posts to the context
        # context['blog_page'] = self
        context['posts'] = self.posts
        return context
    
    # Define a method to get the posts that are descendants of the blog page
    def get_posts(self):
        return PostPage.objects.descendant_of(self).live()
    
    
    # route for the posts filtered according to tags
    @route(r'^tag/(?P<tag>[-\w]+)/$')
    def post_by_tag(self, request, tag, *args, **kwargs):
        self.posts = self.get_posts().filter(tags__slug=tag)
        return self.render(request)
    
    # route for the posts filtered according to categories
    @route(r'^category/(?P<category>[-\w]+)/$')
    def post_by_category(self, request, category, *args, **kwargs):
        self.posts = self.get_posts().filter(categories__blog_category__slug=category)
        return self.render(request)
    
    # Define a route for the blog page that shows the list of posts
    @route(r'^$')
    def post_list(self, request, *args, **kwargs):
        # Assign the posts to a variable
        self.posts = self.get_posts()
        return self.render(request)
    
    # Define another method to get the context for rendering the blog page
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # context['blog_page'] = self
        context['posts'] = self.posts
        return context

# added metatdata functionality to PostPage class
class PostPage (MetadataPageMixin, Page):
    header_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL , related_name="+")
    tags = ClusterTaggableManager(through= "PostPageTags", blank=True)
    body = StreamField([
    ('heading', blocks.TextBlock(form_classname="title")),
    ('special_intro', blocks.TextBlock(max_length=200)),
    ('published_at', blocks.DateBlock(required='True')),
    ('paragraph1', blocks.TextBlock(max_length=250, min_length=200)),
    ('image1', ImageChooserBlock()),
    ('quotation', blocks.TextBlock()),
    ('mini_para', blocks.TextBlock()),
    ('paragraphs', blocks.TextBlock()),
    ], block_counts={
        'heading': {'min_num': 1},
        'paragraphs': {'max_num': 1 },
    }, use_json_field=True)
    content_panels = Page.content_panels + [
        FieldPanel("header_image"),
        FieldPanel("tags"),
        FieldPanel('body'),
        InlinePanel("categories", label="category"),
    ]

    # Define a method to get the context for rendering the post page
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # context['blog_page'] = self.get_parent().specific

        # Add similar posts based on category to the context
        context['similar_posts'] = self.get_similar_posts()

        return context
    
    def get_similar_posts(self):
        # Get the first category associated with this post
        category = self.categories.first()

        # If there is a category, get other posts in the same category
        if category:
            similar_posts = PostPage.objects.live().filter(categories__blog_category=category.blog_category).exclude(id=self.id).order_by('-last_published_at')[:3]
            return similar_posts
        else:
            return None

# intermediary class that connects PostPage to categories, for storage of data into the database
class PostPageBlogCategory(models.Model):
    page = ParentalKey("garage.PostPage", on_delete=models.CASCADE, blank=True, related_name="categories" )
    blog_category = models.ForeignKey("BlogCategory", on_delete=models.CASCADE, related_name="post_page"  )

    panels = [
        FieldPanel("blog_category"),
    ]
    class Meta:
        unique_together = ("page","blog_category")

# model for connecting PostPage to tags, for database storage
class PostPageTags(TaggedItemBase):
    content_object = ParentalKey("PostPage", blank=True, related_name="post_tags" )

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=80, unique=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name ="Category"
        verbose_name_plural ="Categories"

    def __str__(self):
        return self.name
    
@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True