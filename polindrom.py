import time
"""
определяет максимальное число-полиндром,
полученное путем произведения трехзначных чисел
"""
def poly():
    list_poly=[]
    for i in range(800, 1000):
        for j in range(800, 1000):
            if str(i * j) == str(i * j)[::-1]:
                list_poly.append(i * j)
    for i in range(800, 1000):
        for j in range(800, 1000):
            if i * j == max(list_poly):
                print(f"число-полиндром: {max(list_poly)}, число 1: {i}, число 2: {j}")

srart=time.time()
poly()
print(time.time()-srart)