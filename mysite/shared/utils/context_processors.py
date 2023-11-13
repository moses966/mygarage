
from quote_request.models import FormPage

def form_data(request):
    # Fetch the data for the form
    try:
        form_page = FormPage.objects.first()  # Get the first FormPage instance
        form = form_page.specific
    except FormPage.DoesNotExist:
        form = None

    return {
        'form_data': form,
    }
