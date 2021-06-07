class Person:
    instances = 0
    def __init__(self, first_name, last_name, age):
        Person.instances += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        pass

    @classmethod
    def count_instances(cls):
        return f"you have created {cls.instances} instances of {cls.__name__} class"
    
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def is_above_18(self):
        return self.age>18
    

p1 = Person("Rushikesh", "Gaikwad", 16)
p2 = Person("Harshit", "Vashisht", 18)
print(p1.full_name())
print(Person.count_instances())


