class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = price
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    def make_a_call(self, phone_number):
        return f"Calling {phone_number}...."


class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera


p1 = Phone("Nokia", "1100", 1000)
p2 = Smartphone("Oneplus", "6T", 30000, "6 GB", "128 GB", "20 MP")
print(p1.full_name())
print(p2.full_name())
print(p2.internal_memory)

 