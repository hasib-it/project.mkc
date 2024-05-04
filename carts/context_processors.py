from .models import Cart, CartItem
from .views import _cart_id

def cart_id(request):
    # Retrieve or generate cart ID for the current user
    cart_id = request.session.get('cart_id')
    if not cart_id:
        cart_id = _cart_id(request)  # Replace this with your cart ID generation logic
        request.session['cart_id'] = cart_id  # Store the cart ID in the session
    return cart_id
    

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}

    else:
        try:
            cart = Cart.objects.filter(cart_id=cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)
