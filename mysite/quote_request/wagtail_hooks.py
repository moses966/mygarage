from django.urls import path, reverse
from wagtail.admin.menu import MenuItem
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

# Use the '@hooks.register' decorator to register a custom menu item in the Wagtail admin interface.
@hooks.register('register_admin_menu_item')
def register_forms_menu_item():
    
    # Define a function called 'register_forms_menu_item' that will be executed when registering the menu item.
    # Create a menu item labeled 'Forms' in the admin interface. The item links to the 'forms' URL and
    # displays an icon with the name 'form' next to it.

    return MenuItem('Forms', reverse('forms'), icon_name='form')