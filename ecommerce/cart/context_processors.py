from .cart import Cart

def cart(request):
     
     #return default data of cart
     return {'cart': Cart(request)}







