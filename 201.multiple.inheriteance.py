class A:

    def nothing_a(self):
        return "I am just a class A function"
        
    def hello(self):
        return "Hello from class A"

class B:

    def nothing_b(self):
        return "I am just a class B function"

    def hello(self):
        return "Hello from class B"

class C(B,A):
    pass

inherted_c = C()

print(inherted_c.nothing_a())
print(inherted_c.nothing_b())
print(inherted_c.hello())
print(C.__mro__)
print(C.mro())
print(help(C))


