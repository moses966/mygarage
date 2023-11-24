
from wagtail.blocks import StructBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks


class AboutBlock(StructBlock):
    heading = blocks.CharBlock(max_length='45')
    intro = blocks.CharBlock(max_length='250')
    mini_para1 = blocks.CharBlock(max_length='120')
    mini_para2 = blocks.CharBlock(max_length='120')
    outro = blocks.CharBlock(max_length='250')
    image1 = ImageChooserBlock()

class GoalBlock(StructBlock):
    header = blocks.RichTextBlock()
    text = blocks.RichTextBlock()
    number = blocks.IntegerBlock()
    image1 = ImageChooserBlock()

class Director(StructBlock):
    heading1 = blocks.RichTextBlock()
    message = blocks.RichTextBlock()
    image1 = ImageChooserBlock()

'''class Faqs(StructBlock):
    question = blocks.CharBlock(max_length='50')
    answer = blocks.CharBlock(max_length='250')'''

