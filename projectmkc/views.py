from django.shortcuts import render
from store.models import Product  # This is correct

def home(request):
    products = Product.objects.all().filter(is_available=True)  # Use 'Product', not 'Products'

    context = {
        'products': products,
    }
    return render(request, 'home.html', context)
