def is_palindrome(phrase):
    cleaned = ''.join(c.lower() for c in phrase if c.isalnum())
    return cleaned == cleaned[::-1]


phrase = input("Введите слово или фразу: ")
print(f"'{phrase}' является палиндромом." if is_palindrome(phrase) else f"'{phrase}' не является палиндромом.")