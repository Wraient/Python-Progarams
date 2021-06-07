class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.__price = price
    
    def make_a_call(self, phone_number):
        return f"Calling {phone_number}...."

    def full_name(self):
        return f"{self.brand} {self.model_name}"

 
p1 = Phone("nokia", "1100", 1000)
print(p1.make_a_call(9860072854))

print(p1._Phone__price)


