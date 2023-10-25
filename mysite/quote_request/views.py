from django.shortcuts import render
from .models import QuoteRequest  # Importing the QuoteRequest model

def quote_request_list(request):
    # Retrieve all quote requests from the database
    quote_requests = QuoteRequest.objects.all()

    return render(request, 'quote_request/quote_request_list.html', {'quote_requests': quote_requests})
