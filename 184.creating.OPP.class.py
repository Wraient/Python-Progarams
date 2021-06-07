class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        print(f"this class got called")

p1 = Person("Rushikesh", "Gaikwad", 69)
p2 = Person("Harshit", "Vashisth", 96)

print(p1.first_name)
print(p1.last_name)
print(p1.age)
print(p2.first_name)
print(p2.last_name)
print(p2.age)

