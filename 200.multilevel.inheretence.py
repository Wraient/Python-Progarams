class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
    
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
    
    def full_name(self):
        return f"Brand:{self.brand}\nModel:{self.model_name}\nRear Camera:{self.rear_camera}\nRam:{self.ram}\nInternal memory:{self.internal_memory}\nPrice:{self.price}"



class FlagshipPhone(Smartphone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera
    

phone = Phone("Nokia", "1100", 1000)
smartphone = Smartphone("Oneplus", "5T", 30000, "6 GB", "64 GB", "20 MP")
flagshipphone = FlagshipPhone("Oneplus", "6T", 50000, "8 GB", "128 GB", "20 MP", "16 MP")
print(phone.full_name())
print("\n")
print(smartphone.full_name())
print("\n")
print(flagshipphone.full_name())
print("\n")
print(flagshipphone.make_a_call(9561092854))
# print(help(Smartphone))


print(isinstance(phone, Phone))
print(isinstance(smartphone, Phone))
print(isinstance(flagshipphone, Phone))
print(isinstance(smartphone, Smartphone))
print(isinstance(flagshipphone, Smartphone))
print(isinstance(flagshipphone, FlagshipPhone))
print(isinstance(smartphone, FlagshipPhone))
print(isinstance(phone, FlagshipPhone))
print(isinstance(phone, Smartphone))


