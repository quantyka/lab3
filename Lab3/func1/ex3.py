def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None


heads = int(input("Введите количество голов: "))
legs = int(input("Введите количество ног: "))
result = solve(heads, legs)
if result:
    print(f"Курицы: {result[0]}, Кролики: {result[1]}")
else:
    print("Решение не найдено.")