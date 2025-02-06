def grams_to_ounces(grams):
    return grams / 28.3495231


grams = float(input("Введите количество граммов: "))
print(f"{grams} грамм = {grams_to_ounces(grams):.2f} унций")