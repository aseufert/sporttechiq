
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.search import index

from home.blocks import TwoColumnBlock, SectionHeading, CenteredBlock


class HomePage(Page):
    heading = models.CharField(max_length=255, blank=True)
    video = models.URLField(blank=True)
    image_1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image_2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image_3 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField(
        [
            ('heading', SectionHeading()),
            ('centered', CenteredBlock()),
            ('image', ImageChooserBlock()),
            ('embed', EmbedBlock()),
            ('two_columns', TwoColumnBlock()),
            ('HTML', blocks.RawHTMLBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('video'),
        ImageChooserPanel('image_1'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image_3'),
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
