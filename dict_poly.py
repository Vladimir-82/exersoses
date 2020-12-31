import math
def insert_factorial():
    """
    сумма цивр факториал 100 math
    :return:
    """
    res = math.factorial(100)
    return str(sum(int(x) for x in str(res)))

def manual_fuctorial():
    """
        сумма цивр факториал 100 вручную
        :return:
        """
    i = 1
    res = 1
    while i <= 100:
        res = res * i
        i += 1
    return str(sum(int(x) for x in str(res)))



print(insert_factorial())
print(manual_fuctorial())

