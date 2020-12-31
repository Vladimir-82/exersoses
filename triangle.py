def triangle(a):
    b = a * 2
    c = (a ** 2 + b ** 2) ** 0.5
    return b, c

a = 1
print(triangle(a))