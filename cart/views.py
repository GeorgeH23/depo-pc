from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product
from django.contrib import messages

# Create your views here.

def view_cart(request):
    """ A view to return the cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    quantity_str = request.POST.get('quantity')
    redirect_url = request.POST.get('redirect_url')
    stock = None
    
    if 'in_stock' in request.POST:
        stock = request.POST['in_stock']

    if not quantity_str or not quantity_str.isdigit():
        messages.error(request, 'Invalid quantity.')
        return redirect(redirect_url)

    quantity = int(quantity_str)

    cart = request.session.get('cart', {})

    if stock:
        if item_id in list(cart.keys()):
            if stock in cart[item_id]['items_stock'].keys():
                cart[item_id]['items_stock'][stock] += quantity
            else:
                cart[item_id]['items_stock'][stock] = quantity
        else:
            cart[item_id] = {'items_stock': {stock: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart

    product = get_object_or_404(Product, pk=item_id)
    if not product.in_stock:
        messages.warning(request, 'This product is out of stock.')

    return redirect(redirect_url)


def adjust_cart(request, item_id):
    quantity_str = request.POST.get('quantity')
    stock = None
    
    if 'in_stock' in request.POST:
        stock = request.POST['in_stock']

    if quantity_str is None or not quantity_str.isdigit():
        messages.error(request, 'Invalid quantity.')
        return redirect(reverse('view_cart'))

    quantity = int(quantity_str)

    cart = request.session.get('cart', {})

    if stock:
        if quantity > 0:
            cart[item_id]['items_stock'][stock] = quantity
        else:
            del cart[item_id]['items_stock'][stock]
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            del cart[item_id]

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))

