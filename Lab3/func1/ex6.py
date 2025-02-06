def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])


sentence = input("Введите предложение: ")
print(f"Перевёрнутое предложение: {reverse_words(sentence)}")