from django.shortcuts import render


def error_400_view(request, exception):
    return render(request, 'errors/400.html')


def error_403_view(request, exception):
    return render(request, 'errors/403.html')


def error_404_view(request, exception):
    return render(request, 'templates/errors/404.html')


def error_500_view(request):
    return render(request, 'errors/500.html')
