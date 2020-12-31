def roud():
    """
    Рассмотрим все целочисленные комбинации ab для 2 ≤ a ≤ 5 и 2 ≤ b ≤ 5:

    22=4, 23=8, 24=16, 25=32
    32=9, 33=27, 34=81, 35=243
    42=16, 43=64, 44=256, 45=1024
    52=25, 53=125, 54=625, 55=3125

    Если их расположить в порядке возрастания, исключив повторы,
    мы получим следующую последовательность из 15 различных членов:

    4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

    Сколько различных членов имеет последовательность ab для 2 ≤ a ≤ 100 и 2 ≤ b ≤ 100?
    :return:
    """
    num_list=[]
    for i in range(2, 101):
        for j in range(2, 101):
            num_list.append(i**j)
    return len(set(num_list))

if __name__ == "__main__":
    print(roud())