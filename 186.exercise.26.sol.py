class Laptop:
    def __init__(self, brand, name, price):
        # instance variables
        self.brand = brand
        self.name = name
        self.price = price
        self.laptop_name = brand + " " + name


laptop1 = Laptop("Sony", "Panasonic", 69000)
laptop2 = Laptop("Redmi", "Microsoft", 69)

print(laptop1.name)
print(laptop2.brand)
print(laptop1.laptop_name)