class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def phone_name(self):
        return f"{self.brand} {self.model}"
    
    def __str__(self):
        return f"{self.brand} {self.model} and price is {self.price}"

    def __repr__(self):
        return f"Phone(\"{self.brand}\", \"{self.model}\", {self.price})"

    def __len__(self):
        
        return len(self.phone_name())

    def __add__(self, other):
        return self.price + other.price

    def __mul__(self, other):
        return self.price * other.price

phone1 = Phone("Nokia", "1100", 1000)
phone2 = Phone("Nokia", "1600", 1200)
# print(phone1) # For common user
# print(repr(phone1)) # For Developer
# print(phone1.__repr__())
# print(phone1.__len__())
# print(phone1 + phone2)
# print(phone1 * phone2)

