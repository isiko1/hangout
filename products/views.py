from django.shortcuts import render

# Create your views here.


def products(request):
    """ A view to the products page """
    context = {}
    return render(request, 'products/products.html', context)
