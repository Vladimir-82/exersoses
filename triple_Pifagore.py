import time
def pifagore():
    """
    Тройка Пифагора — три натуральных числа a < b < c, для которых выполняется равенство

    a2 + b2 = c2

    Например, 32 + 42 = 9 + 16 = 25 = 52.

    Существует только одна тройка Пифагора, для которой a + b + c = 1000.
    Найдите эти числа
    :return:
    """
    per = 1000
    for i in range(1, per):
        for j in range(i+1, per):
            k = per - i - j
            if i**2 + j**2 == k**2:
                print(i, j, k)

start = time.time()
pifagore()
print(time.time() - start)