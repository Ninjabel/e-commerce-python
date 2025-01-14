class Product:
    products_db = []

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        Product.products_db.append(self)

    @classmethod
    def get_all_products(cls):
        return cls.products_db

    @classmethod
    def get_product_by_id(cls, product_id):
        for product in cls.products_db:
            if product.product_id == product_id:
                return product
        return None

    @classmethod
    def delete_product(cls, product_id):
        product_to_delete = cls.get_product_by_id(product_id)
        if product_to_delete:
            cls.products_db.remove(product_to_delete)
            return True
        return False

    @classmethod
    def update_product(cls, product_id, name=None, price=None):
        product = cls.get_product_by_id(product_id)
        if product:
            if name:
                product.name = name
            if price is not None:
                product.price = price
            return True
        return False
