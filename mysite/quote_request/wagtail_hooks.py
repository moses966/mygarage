from django.urls import path
from wagtail import hooks

from .views import quote_request_list

# Define a function called 'register_forms_url' that registers a custom URL pattern for the Wagtail admin interface.
@hooks.register('register_admin_urls')
def register_forms_url():

     # Create a URL pattern for the '/forms/' URL that maps to the 'quote_request_list' view function.
    # This allows us to access the 'quote_request_list' view at the '/admin/forms/' URL.
    # Also, give this URL pattern the name 'forms' for easy reference.
    
    return [
        path('forms/', quote_request_list, name='forms'),
    ]