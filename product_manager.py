from product import Product
class ProductManager():
    def __init__(self):
        self.products = Product.Product_list
    
    def add_product(self,product):
        if product not in self.products:
            self.products.append(product)  
       
   
    def show_products(self):
        return self.products
    
    def suma_vrijednosti(self):
        return f"${round(sum(item.price for item in self.products),2)}"
    
    def remove_product(self,product):
        self.products.remove(product)
