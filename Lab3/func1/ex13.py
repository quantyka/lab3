def guess_the_number():
    import random
    print("Привет! Как тебя зовут?")
    name = input()
    print(f"Ну что, {name}, я загадал число от 1 до 20.")
    number = random.randint(1, 20)
    attempts = 0
    while True:
        guess = int(input("Попробуй угадать: "))
        attempts += 1
        if guess < number:
            print("Твоё число слишком маленькое.")
        elif guess > number:
            print("Твоё число слишком большое.")
        else:
            print(f"Поздравляю, {name}! Ты угадал число за {attempts} попыток!")
            break


guess_the_number()