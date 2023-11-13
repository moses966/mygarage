from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel
from taggit.models import Tag as TaggitTag, TaggedItemBase
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock



class BlogPage(Page):
    description = models.CharField(max_length=250, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]

class PostPage (Page):
    header_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL , related_name="+")
    tags = ClusterTaggableManager(through= "PostPageTags", blank=True)
    body = StreamField([
    ('heading', blocks.CharBlock(form_classname="title")),
    ('published_at', blocks.DateBlock(required='True')),
    ('paragraph', blocks.RichTextBlock()),
    ('image', ImageChooserBlock()),
    ], block_counts={
        'heading': {'min_num': 1},
        'image': {'max_num': 5},
    }, use_json_field=True)
    content_panels = Page.content_panels + [
        FieldPanel("header_image"),
        FieldPanel("tags"),
        FieldPanel('body'),
        InlinePanel("categories", label="category"),
    ]


class PostPageBlogCategory(models.Model):
    page = ParentalKey("garage.PostPage", on_delete=models.CASCADE, blank=True, related_name="categories" )
    blog_category = models.ForeignKey("BlogCategory", on_delete=models.CASCADE, related_name="post_page"  )

    panels = [
        FieldPanel("blog_category"),
    ]
    class Meta:
        unique_together = ("page","blog_category")

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