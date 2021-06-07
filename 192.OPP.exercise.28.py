class Person:
    instance = 0
    def __init__(self):
        instance += 1
        self.count_instance = instance
        pass

p1 = Person()
p2 = Person()
print(Person.count_instance)



