from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from .blocks import AboutBlock, Director, Faqs, GoalBlock


class AboutPage(Page):
    body = StreamField([
        ('about_block', AboutBlock()),
        ('about_director', Director()),
        ('faqs', Faqs()),
        ('goals', GoalBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]