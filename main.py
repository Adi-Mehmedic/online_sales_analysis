from product_manager import ProductManager
from product import Product
from cart import Cart
#Dodavanje Korpe
Korpa = Cart()
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
#Dodavanje u korpu
Korpa.add_items(Banana)
Korpa.add_items(Orange)
Korpa.add_items(Potato)
#Ispis naplate i sadrzaj korpe
print(Korpa.naplata())
print(Korpa.prikaz_korpe())

