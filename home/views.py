from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """
    context = {}
    return render(request, 'home/index.html', context)


def bag(request):
    """ A view to the shopping bag page """
    context = {}
    return render(request, 'home/bag.html', context)


def checkout(request):
    """ A view to the checkout page """
    context = {}
    return render(request, 'home/checkout.html', context)
