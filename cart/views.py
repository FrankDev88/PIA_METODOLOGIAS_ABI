from django.shortcuts import render

# Create your views here.
# session_cart_app/cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from food.models import FoodItem  # Ajusta 'your_app'

from django.http import JsonResponse

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(FoodItem, id=product_id)
    cart.add(product=product, quantity=1)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'cart_items_count': len(cart)})
    
    return redirect('cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(FoodItem, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

from django.shortcuts import render, get_object_or_404
from .cart import Cart
from food.models import FoodItem

def cart_detail(request):
    cart = Cart(request)
    cart_items = []

    # Los IDs de los productos en el carrito
    product_ids = cart.cart.keys()

    # Consulta todos los productos de la base de datos cuyos IDs estén en el carrito
    products = FoodItem.objects.filter(id__in=product_ids)

    for product in products:
        quantity = cart.cart[str(product.id)]['quantity']
        total_price = float(product.price) * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': total_price,
        })

    # Calcula subtotal general
    subtotal = sum(item['total_price'] for item in cart_items)

    context = {
        'cart_items': cart_items,
        'cart_subtotal': subtotal,
    }
    return render(request, 'cart.html', context)



@require_POST
def cart_update_quantity(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(FoodItem, id=product_id)
    try:
        quantity = int(request.POST.get('quantity', 1))
    except ValueError:
        quantity = 1

    if quantity > 0:
        cart.add(product=product, quantity=quantity, update_quantity=True)
    else:
        cart.remove(product)

    return redirect('cart_detail')


from django.shortcuts import render, redirect
from django.http import JsonResponse

def checkout(request):
    if request.method == 'POST':
        # Vaciar carrito
        request.session['cart'] = {}
        # Retornar JSON de éxito
        return JsonResponse({'success': True})
