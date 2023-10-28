from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

# Define a custom form field that is associated with a FormPage
class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='custom_form_fields')

# Define a FormPage model, which inherits from AbstractEmailForm
class FormPage(AbstractEmailForm):
    # Introduction text for the form page
    intro = RichTextField(blank=True)
    # Thank you text to display after successful form submission
    thank_you_text = RichTextField(blank=True)

    # Define content panels for the FormPage
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('custom_form_fields', label="Form fields"),   # Inline panel for custom form fields
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),    # Email sender address
                FieldPanel('to_address', classname="col6"),  # Email recipient address
            ]),
            FieldPanel('subject'),   # Email subject
        ], "Email"),   # Panel for email configuration
    ]
    
     # Method to get all form fields associated with this FormPage
    def get_form_fields(self):
        return self.custom_form_fields.all()