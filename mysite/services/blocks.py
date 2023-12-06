from wagtail.blocks import StructBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks


class FirstServiceBlock(StructBlock):
    heading = blocks.TextBlock(max_length=120)
    text = blocks.TextBlock()
    image1 = ImageChooserBlock()

class SecondServiceBlock(StructBlock):
    heading = blocks.TextBlock(max_length=120)
    intro = blocks.TextBlock()
    text1 = blocks.TextBlock(max_length=30)
    text2 = blocks.TextBlock(max_length=30)
    text3 = blocks.TextBlock(max_length=30)
    text4 = blocks.TextBlock(max_length=30)
    text5 = blocks.TextBlock(max_length=30)
    text6 = blocks.TextBlock(max_length=30)
    outro = blocks.TextBlock()
    image1 = ImageChooserBlock()

class BodyBlock(StructBlock):
    heading = blocks.TextBlock(max_length=30)
    intro = blocks.TextBlock()
    image1 = ImageChooserBlock()
    paragraph1 = blocks.TextBlock()
    paragraph2 = blocks.TextBlock()
    thought1 = blocks.RichTextBlock()
    thought2 = blocks.RichTextBlock()
    paragraphs = blocks.TextBlock()
    post_number = blocks.IntegerBlock()