class Animals:
    def __init__(self, name):
        self.name = name
    
    def sounds(self):
        raise NotImplementedError("You have to define this method in subclass ")


class Dog(Animals):
    def __init__(self, name, bread):
        super().__init__(name)
        self.bread = bread
    
    def sounds(self):
        return "Bhaw Bhaw"

class Cat(Animals):
    def __init__(self, name, bread):
        super().__init__(name)
        self.bread = bread
    

doggy = Dog("Dog", "pog")
cat = Cat("cat", "abc")
print(doggy.sounds())
print("\n")
print(cat.sounds())
