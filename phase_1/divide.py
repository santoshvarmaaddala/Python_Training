# performing division and modulus opeator without using /,%,//

a = int(input())
b = int(input())
i = 0
while a >= b:
    a -= b
    i += 1
print("quotient is ", i, "remainder is", a);
