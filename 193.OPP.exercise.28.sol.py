class Person:
    instance = 0
    def __init__(self, name, last_name, age):
        Person.instance +=1
        self.name = name
        self.last_name = last_name
        self.age = age
        pass

p1 = Person("Harshit", "Vashishth", 69)
p2 = Person("rushikesh", "Gaikwad", 70)
p3 = Person("Harshit", "Vashishth", 69)
p4 = Person("rushikesh", "Gaikwad", 70)
print(Person.instance)



