# session_cart_app/cart/context_processors.py
from .cart import Cart

def cart_counter(request):
    cart = Cart(request)
    return {'cart_items_count': len(cart)}