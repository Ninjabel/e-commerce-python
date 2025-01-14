class Order:
    orders_db = []

    def __init__(self, order_id, user_id, products):
        self.order_id = order_id
        self.user_id = user_id
        self.products = products
        Order.orders_db.append(self)

    @classmethod
    def get_all_orders(cls):
        return cls.orders_db

    @classmethod
    def get_order_by_id(cls, order_id):
        for order in cls.orders_db:
            if order.order_id == order_id:
                return order
        return None

    @classmethod
    def delete_order(cls, order_id):
        order_to_delete = cls.get_order_by_id(order_id)
        if order_to_delete:
            cls.orders_db.remove(order_to_delete)
            return True
        return False

    @classmethod
    def update_order(cls, order_id, user_id=None, products=None):
        order = cls.get_order_by_id(order_id)
        if order:
            if user_id:
                order.user_id = user_id
            if products:
                order.products = products
            return True
        return False
