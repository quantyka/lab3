def filter_prime(numbers):
    import math
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return [n for n in numbers if is_prime(n)]


numbers = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Простые числа: {filter_prime(numbers)}")