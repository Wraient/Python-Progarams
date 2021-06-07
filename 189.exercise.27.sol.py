class Laptop:
    def __init__(self, brand, name, price):
        # instance variables
        self.brand = brand
        self.name = name
        self.price = price
        self.laptop_name = brand + " " + name
    def apply_discount(self, num):
        self.discount = num
        off_price = (num/100)*self.price
        return (self.price - off_price)

laptop1 = Laptop("hp", "au11rtx", 63000)
laptop2 = Laptop("apple", "macbook pro", 230000)
print(laptop1.apply_discount(10))
print(laptop2.apply_discount(10))
