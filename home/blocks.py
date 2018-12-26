from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ColumnBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = 'home/blocks/column.html'


class TwoColumnBlock(blocks.StructBlock):
    left_column = ColumnBlock(icon='arrow-right', label='Left column content')
    right_column = ColumnBlock(icon='arrow-right', label='Right column content')

    class Meta:
        template = 'home/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class SectionHeading(blocks.StructBlock):
    heading = blocks.CharBlock()

    class Meta:
        template = 'home/blocks/section_heading.html'
        icon = 'placeholder'
        label = 'Section Heading'