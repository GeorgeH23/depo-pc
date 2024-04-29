from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """
    num_items = 3
    captions = [
        {'title': 'Desktop PCs'},
        {'title': 'Laptops'},
        {'title': 'Accessories'}
    ]

    for i in range(len(captions)):
        captions[i]['index'] = i + 1

    context = {
        'num_items': num_items,
        'captions': captions,
    }

    return render(request, 'home/index.html', context)
