import math
import time
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


start=time.time()
print(insert_factorial())
print(time.time()-start)

start=time.time()
print(manual_fuctorial())
print(time.time()-start)
