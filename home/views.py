from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def checkout(request):
    """ A view to the checkout page """
    context = {}
    return render(request, 'home/checkout.html', context)
