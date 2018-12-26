from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.search import index
from django.db import models

from home.blocks import TwoColumnBlock, SectionHeading


class HomePage(Page):
    header = models.CharField(max_length=255, blank=True)
    header_description = models.CharField(max_length=255, blank=True)
    body = StreamField([
            ('heading', SectionHeading()),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embed', EmbedBlock()),
            ('two_columns', TwoColumnBlock()),
            ('HTML', blocks.RawHTMLBlock()),
        ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        FieldPanel('header_description'),
        StreamFieldPanel('body', classname="full"),
    ]


class BasicPage(Page):
    heading = models.CharField(max_length=255, blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
        ('two_columns', TwoColumnBlock()),
        ('HTML', blocks.RawHTMLBlock()),
    ], null=True, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('heading'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('heading', classname="main-heading"),
        StreamFieldPanel('body', classname="full"),
    ]