from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Product, Category, Favorite
from .forms import ProductForm

# Create your views here.

def all_products(request):
    """ A view to return all products page """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    product_in_favorites = {}
    favorite_ids = []

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criterial!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    if request.user.is_authenticated:
        favorite_instance = Favorite.objects.filter(user=request.user).first()
        favorite_products = favorite_instance.products.all()
        favorite_ids = [product.id for product in favorite_products]
    
    redirect_url = request.POST.get('redirect_url')

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'product_in_favorites': favorite_ids,
        'redirect_url': redirect_url,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view for the product details """

    product = get_object_or_404(Product, pk=product_id)
    product_in_favorites = {}
    favorite_ids = []
    redirect_url = request.POST.get('redirect_url')

    if request.user.is_authenticated:
            favorite_instance = Favorite.objects.filter(user=request.user).first()
            favorite_products = favorite_instance.products.all()
            favorite_ids = [product.id for product in favorite_products]

    context = {
        'product': product,
        'product_in_favorites': favorite_ids,
        'redirect_url': redirect_url,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
 
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def favorite_view(request):
    """ Display products from Favorite """
    favorite = Favorite.objects.all()
    context = {
        'f': favorite
    }

    return render(request, 'products/favorite.html', context)


@login_required
def add_to_favorite(request, product_id):
    """ Add a product to the Favorite """
    try:
        product = Product.objects.get(id=product_id)
        favorite, created = Favorite.objects.get_or_create(user=request.user)
        favorite.products.add(product)
        context = {"bool": True}
    except Product.DoesNotExist:
        context = {"bool": False, "message": "Product does not exist."}

    return JsonResponse(context)


@login_required
def remove_from_favorite(request, product_id):
    """ Remove a product from the Favorite """
    favorite = Favorite.objects.get(user=request.user)
    product_instance = Product.objects.get(id=product_id)
    favorite.products.remove(product_instance)

    favorite.save()
    favorite = Favorite.objects.all()

    # Pass the redirect_url to the template
    redirect_url = request.POST.get('redirect_url')

    context = {
        "f": favorite,
        'redirect_url': redirect_url,
    }

    return render(request, 'products/favorite.html', context)
