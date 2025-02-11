class Product():
    Product_list = []
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.Product_list.append(self)

    def __repr__(self):
        return f"{self.name} - ${self.price:.2f}"
        

    def show_info(self):
        return f"Name: {self.name} \n price: {self.price} \n quantity: {self.quantity}"
    
    def change_quantity(self,quantity):
        self.quantity = quantity
