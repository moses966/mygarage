from wagtail.blocks import StructBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks


# main carousel content
class CarouselBlock(StructBlock):
    heading1 = blocks.TextBlock()
    text1 = blocks.TextBlock()
    heading2 = blocks.TextBlock()
    text2 = blocks.TextBlock()
    heading3 = blocks.TextBlock()
    text3 = blocks.TextBlock()

# carousel content
class CarouselBlock1(StructBlock):
    heading = blocks.TextBlock()
    intro = blocks.TextBlock()

# carousel content
class CarouselBlock2(StructBlock):
    heading = blocks.TextBlock()
    intro = blocks.TextBlock()

# carousel content
class CarouselBlock3(StructBlock):
    heading = blocks.TextBlock()
    intro = blocks.TextBlock()

# block below the carousel
class HomeBlock1(StructBlock):
    heading = blocks.TextBlock()
    intro = blocks.TextBlock()
    image1 = ImageChooserBlock()
    sub_header1 = blocks.TextBlock()
    text1 = blocks.TextBlock()
    image2 = ImageChooserBlock()
    sub_header2 = blocks.TextBlock()
    text2 = blocks.TextBlock()

# block just below the featurate
class HomeBlock2(StructBlock):
    heading = blocks.TextBlock()
    image1 = ImageChooserBlock()
    sub_header1 = blocks.TextBlock()
    text1 = blocks.TextBlock()
    image2 = ImageChooserBlock()
    sub_header2 = blocks.TextBlock()
    text2 = blocks.TextBlock()

# second last block
class HomeBlock3(StructBlock):
    heading = blocks.TextBlock()
    intro = blocks.TextBlock()
    image1 = ImageChooserBlock()
    sub_header1 = blocks.TextBlock()
    text1 = blocks.TextBlock()
    image2 = ImageChooserBlock()
    sub_header2 = blocks.TextBlock()
    text2 = blocks.TextBlock()
    image3 = ImageChooserBlock()
    sub_header3 = blocks.TextBlock()
    text3 = blocks.TextBlock()

# How it works block
class HomeBlock4(StructBlock):
    heading = blocks.TextBlock()
    intro = blocks.TextBlock()
    image1 = ImageChooserBlock()
    sub_header1 = blocks.TextBlock()
    text1 = blocks.TextBlock()
    image2 = ImageChooserBlock()
    sub_header2 = blocks.TextBlock()
    text2 = blocks.TextBlock()
    image3 = ImageChooserBlock()
    sub_header3 = blocks.TextBlock()
    text3 = blocks.TextBlock()