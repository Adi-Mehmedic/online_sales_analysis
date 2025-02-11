from product_manager import ProductManager
from product import Product
#ProductManager
Adi = ProductManager()
#Products
Tomato = Product("Tomato",1.3,10)
Potato = Product("Potato",0.8,30)
Banana = Product("Banana",1.8,25)
Orange = Product("Orange",1.45,18)
#Ispis produkta 
print(Adi.show_products())
#Dodavanje novog producta
Adi.add_product(Product("Grapes",2.1,15))
print(Adi.show_products())
#Suma cijena
print(Adi.suma_vrijednosti())
#Uklanjanje producta
Adi.remove_product(Orange)
print(Adi.show_products())