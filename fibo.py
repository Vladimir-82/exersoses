import time

def fibo():
    """
    Каков порядковый номер первого члена последовательности Фибоначчи, содержащего 1000 цифр?
    :return:
    """
    lst=[]
    k = 1
    i = 1
    j = 1
    lst.append(i)
    lst.append(j)
    while len(str(k))<=1000:
        k = i + j
        lst.append(k)
        i = j
        j = k
    print(lst[-1])
    print(lst.index(lst[-1]))

if __name__ == "__main__":
    start=time.time()
    fibo()
    print(time.time()-start)