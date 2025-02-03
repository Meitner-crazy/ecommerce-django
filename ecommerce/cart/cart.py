from decimal import Decimal  # Prices
from store.models import Product


class Cart():

    def __init__(self, request):

        self.session = request.session

        # returning user - obtain his/her existing session
        cart = self.session.get('session_key')

        # new user - generate a new session
        if 'session_key' not in request.session:

            cart = self.session['session_key'] = {}

        self.cart = cart

    
    def add(self, product, product_qty):

        product_id = str(product.id)

        if product_id in self.cart:

            self.cart[product_id]['qty'] = product_qty # modify the quantity accordingly

        else:

            self.cart[product_id] =  {'price': str(product.price), 'qty': product_qty} 
            #add a new product with price and qty passing over together --> dictionary

        self.session.modified = True



    def delete(self, product):

        product_id = str(product)

        if product_id in self.cart:

            del self.cart[product_id]

        self.session.modified = True



    def update(self, product, qty):
        
        product_id = str(product)
        product_quantity = qty

        if product_id in self.cart:

            self.cart[product_id]['qty'] = product_quantity
        
        self.session.modified = True



    
    def __len__(self):

        return sum(item['qty'] for item in self.cart.values())


    def __iter__(self): # Iterate all the products in the cart

        all_product_ids = self.cart.keys()

        # __in --> syntax in the context of filtering data or querying database
        products = Product.objects.filter(id__in=all_product_ids)

        # optimize by deep copy
        # cart = self.cart.copy()
        import copy

        cart = copy.deepcopy(self.cart)

        for product in products:

            cart[str(product.id)]['product'] = product


        for item in cart.values(): # convert price string to decimal
            
            item['price'] = Decimal(item['price'])

            item['total'] = item['price'] * item['qty']

            yield item

    def get_total(self):

        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())















