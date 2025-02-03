from django.shortcuts import render

from .cart import Cart

from store.models import Product
from django.shortcuts import get_object_or_404

from django.http import JsonResponse 


# Create your views here.
def cart_summary(request):

    cart = Cart(request)

    return render(request, 'cart/cart-summary.html', {'cart': cart})




def cart_add(request):
    
    cart = Cart(request)

    if request.POST.get('action') == 'post':

        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        #get the product from the CLASS Product where the id equals to the product_id
        product = get_object_or_404(Product, id=product_id)

        # get the product along with the quantity --> so we need create an add() in Class Cart
        cart.add(product=product, product_qty=product_quantity)

        cart_quantity = cart.__len__() # total quantity of cart of session data

        response = JsonResponse({'qty': cart_quantity})

        return response
    

def cart_delete(request):
     
    cart = Cart(request)

    if request.POST.get('action') == 'post':

        product_id = int(request.POST.get('product_id'))  #refering to cart-summary.html

        cart.delete(product=product_id)

        cart_quantity = cart.__len__() # total quantity of cart of session data

        cart_total = cart.get_total()

        response = JsonResponse({'qty:' : cart_quantity, 'total':cart_total})

        return response
    
def cart_update(request):

    cart = Cart(request)

    if request.POST.get('action') == 'post':

        product_id = int(request.POST.get('product_id'))  #refering to cart-summary.html
        product_quantity = int(request.POST.get('product_quantity'))

        cart.update(product=product_id, qty=product_quantity)

        cart_quantity = cart.__len__() # total quantity of cart of session data
        cart_total = cart.get_total()

        response = JsonResponse({'qty:':cart_quantity, 'total':cart_total})

        return response
