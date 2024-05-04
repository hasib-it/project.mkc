from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import Paginator
from django.db.models import Q


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)

    paginator = Paginator(products, 3)  # Paginate the products queryset with 3 items per page
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)  # Get the requested page of products
    product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    single_product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)

def search(request):

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            # Filter products based on keyword
            products = Product.objects.filter(
            Q(description__icontains=keyword) | Q(product_name__icontains=keyword)).order_by('-created_date')
            product_count = products.count()  # Update the count based on the query

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)
