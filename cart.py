class Cart():
    def __init__(self):
        self.cart_items = []
    
    def add_items(self,item):
        self.cart_items.append(item)
    
    def naplata(self):
        return f"Ukupna cijena za naplatu je ${round(sum(item.price for item in self.cart_items),2)}"
    
    def prikaz_korpe(self):
        return f" Korpa:{self.cart_items}"