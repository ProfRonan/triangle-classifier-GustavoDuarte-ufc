a = float(input())
b = float(input())
c = float(input())

tri1 = a + b
tri2 = b + c
tri3 = c + a

if tri1 > c and tri2 > a and tri3 > b:
    if a == b and c == b:
        print("Equilátero")
    elif a == b and c != a:
        print("Isósceles")
    elif c == b and a != b:
        print("Isósceles")
    elif c == a and b != c:
        print("Isósceles")
    elif a != c and b != c and a != b:
        print("Escaleno")
else:
    print("Não é um triângulo")
    