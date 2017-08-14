import math

def quad(a, b, c):
    if b**2 - 4*a*c < 0:
        print("cette fonction ne possède aucun zéro")
    else:
        x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        print(x1)
        print(x2)

while True:
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    quad(a, b, c)