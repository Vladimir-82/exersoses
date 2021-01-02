import itertools


# Т.к желаемое число не такое и большое то мы просто идем простым циклом
def compute():
    DIGITS = 1000
    prev = 1
    cur = 0
    for i in itertools.count():
        # На этом шаге, prev = fibonacci(i - 1) и cur = fibonacci(i)
        if len(str(cur)) > DIGITS:
            raise RuntimeError("Not found")
        elif len(str(cur)) == DIGITS:
            return str(i)

        # Пересчитываем prev и cur по формуле чисел Фибоначчи
        prev, cur = cur, prev + cur


if __name__ == "__main__":
    print(compute())