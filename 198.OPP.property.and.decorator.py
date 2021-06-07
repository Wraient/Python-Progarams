class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = max(price,0)
    
    @property
    def full_spec(self):
        return f"{self.brand} {self.model} for {self._price}"

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = max(new_price,0)
        return self.price

    def make_a_call(self, phone_number):
        return f"Calling {phone_number}...."

    def full_name(self):
        return f"{self.brand} {self.model_name}"




p1 = Phone("Nokia", "1100", 1000)
print(p1.price)
p1.price = 500
print(p1.full_spec)



