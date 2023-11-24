from wagtail.blocks import StructBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks


class FirstServiceBlock(StructBlock):
    heading = blocks.CharBlock(max_length=120)
    text = blocks.RichTextBlock()
    image1 = ImageChooserBlock()

class SecondServiceBlock(StructBlock):
    heading = blocks.CharBlock(max_length=120)
    intro = blocks.RichTextBlock()
    text1 = blocks.CharBlock(max_length=30)
    text2 = blocks.CharBlock(max_length=30)
    text3 = blocks.CharBlock(max_length=30)
    text4 = blocks.CharBlock(max_length=30)
    text5 = blocks.CharBlock(max_length=30)
    text6 = blocks.CharBlock(max_length=30)
    outro = blocks.RichTextBlock()
    image1 = ImageChooserBlock()

class BodyBlock(StructBlock):
    heading = blocks.CharBlock(max_length=30)
    core_intro = blocks.CharBlock(max_length=120)
    intro = blocks.RichTextBlock()
    image1 = ImageChooserBlock()
    paragraph1 = blocks.RichTextBlock()
    paragraph2 = blocks.RichTextBlock()
    thought1 = blocks.RichTextBlock()
    thought2 = blocks.RichTextBlock()
    paragraphs = blocks.RichTextBlock()
    post_number = blocks.IntegerBlock()