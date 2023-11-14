from wagtail.blocks import StructBlock, RichTextBlock
from wagtail.images.blocks import ImageChooserBlock

class ParagraphWithImageBlock(StructBlock):
    text = RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = 'blocks/paragraph_with_image.html'