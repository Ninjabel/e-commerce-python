class Cart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []

    def add_product(self, product_id, quantity=1):
        for item in self.items:
            if item['product_id'] == product_id:
                item['quantity'] += quantity
                return
        self.items.append({'product_id': product_id, 'quantity': quantity})

    def remove_product(self, product_id):
        self.items = [item for item in self.items if item['product_id'] != product_id]

    def clear_cart(self):
        self.items = []

    def get_cart_details(self):
        return {'user_id': self.user_id, 'items': self.items}