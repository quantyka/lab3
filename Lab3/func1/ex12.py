def histogram(lst):
    for num in lst:
        print('*' * num)


lst = list(map(int, input("Введите числа через пробел: ").split()))
print("Гистограмма:")
histogram(lst)