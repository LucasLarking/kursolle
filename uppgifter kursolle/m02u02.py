a = 9
b = 2
f = 4.0
namn = 'Lucas Larking'

print(a * b, type(a*b))
print(a * f, type(a*f))
print(a / b, type(a/b)) # därför det 4.5 är inte heltal
print(namn, type(namn))
print(int(a / b), type(int(a/b))) # heltalet avrundat nedåt blir 4, det är int
print(a % b, type(a % b)) # resten är 1, 1 är en int
print(a ** 0.5, type(a ** 0.5)) # roten ur 9=3
print(b**2, type(b**2)) # 2^2=4, 4 är int
print(f**2, type(b**2)) #4^2=16, 16 är int
a += b
print(a)