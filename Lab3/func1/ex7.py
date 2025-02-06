def has_33(nums):
    return any(nums[i] == 3 and nums[i + 1] == 3 for i in range(len(nums) - 1))


nums = list(map(int, input("Введите числа через пробел: ").split()))
print("Список содержит два подряд стоящих числа 3." if has_33(nums) else "Список не содержит два подряд стоящих числа 3.")