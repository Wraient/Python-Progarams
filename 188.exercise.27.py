class Laptop:
    def __init__(self, brand, name, price):
        # instance variables
        self.brand = brand
        self.name = name
        self.price = price
        self.laptop_name = brand + " " + name
    def apply_discount(self, discount):
        self.discount = discount
        self.apply_discount = (self.price/100)*discount
        return self.apply_discount
    

laptop1 = Laptop("hp", "au11rtx", 63000)
print(laptop1.apply_discount(10))


