from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Contact
from .forms import ContactForm


def about(request):
    """ A view to return the index page """

    return render(request, 'support/about.html')


def subscribe(request):
    """ A view to return the subscribe page """

    return render(request, 'support/subscribe.html')


def t_and_c(request):
    """ A view to return the t&c's page """

    return render(request, 'support/legal/t_and_c.html')


def privacy(request):
    """ A view to return the privacy page """

    return render(request, 'support/legal/privacy.html')


def contact(request):
    """ A view to return the contact page """

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            user_message = form.cleaned_data['message']
            contact_reason = form.cleaned_data['contact_reason']

            # Create an email subject
            subject = f'depoPC - contact about {contact_reason}'

            # Render the email message using a template
            message = render_to_string(
                'support/email_confirmation.txt', {
                    'name': name,
                    'message': user_message
                })

            email_from = settings.DEFAULT_FROM_EMAIL
            email_to = [form.cleaned_data['email']]

            # Send the email
            send_mail(
                subject,
                message,
                email_from,
                email_to
            )
            # Display a success message and redirect to the contact page
            messages.info(request, f'Your message was sent successfuly')
            return redirect(reverse('home'))
        else:
            # Display an error message if form submission fails
            messages.error(
                request, f'An error occured, please try again later')

    context = {
        'form': form,
    }

    return render(request, 'support/contact.html', context)
