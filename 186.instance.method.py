class Person:
    def __init__(self, name, last_name, age):
        # Instances
        self.name = name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.name} {self.last_name}"

    def is_above_18(self):
        return self.age>18


p1 = Person("Rushikesh", "Gaikwad", 69)
p2 = Person("Mohit", "Vashishth", 70)

print(p1.full_name())
print(p1.is_above_18())
print(p1.name)

print(p2.full_name())
print(p2.is_above_18())
print(p2.name)


print(Person.full_name(p1))

