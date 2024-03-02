from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OpuqeHySjuRs6tM9u8CNH4qyP6OTwoEowP7NKeDeGIn5raepweDE5gY3wlvmJaIjQaV4Pk3cJDMTKQpJr0gek5r00dH3xaG8a',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
