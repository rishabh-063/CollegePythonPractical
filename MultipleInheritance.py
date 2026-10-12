class A:
    def __init__(self, a):
        self.a = a

class B:
    def __init__(self, b):
        self.b = b

class C(A, B):
    def __init__(self, a, b, c):
        A.__init__(self, a)
        B.__init__(self, b)
        self.c = c

Object = C(1,2,3)
print("Value of a:", Object.a)
print("Value of b:", Object.b)
print("Value of c:", Object.c)