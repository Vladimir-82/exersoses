import time
print(time.ctime())
print(time.localtime(12))
def name(str):

    lst=str.split()
    return lst[-1] + ' ' + lst[0]



def name_2(str):
    return ' '.join(str.split()[::-1])

n = 'Donald Tramp'
start=time.time()
print(name(n))

print(name_2(n))

print(time.time() - start)