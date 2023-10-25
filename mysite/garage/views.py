'''from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import QuoteRequestForm

def quote_request_view(request):
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database

            # Send email notification
            subject = 'New Quote Request'
            message = 'A new quote request has been submitted. Check the admin panel for details.'
            from_email = 'your_email@example.com'  # Replace with your email
            recipient_list = ['admin_email@example.com']  # Replace with the admin's email

            send_mail(subject, message, from_email, recipient_list)

            return redirect('thank_you_page')  # Redirect to a thank you page

    else:
        form = QuoteRequestForm()

    return render(request, 'quote_request_form.html', {'form': form})'''
