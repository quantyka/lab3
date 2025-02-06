def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


fahrenheit = float(input("Введите температуру в Фаренгейтах: "))
print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.2f}°C")