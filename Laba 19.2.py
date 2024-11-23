import pandas as pd
import os
import re
input_file = "words.txt"
output_file = "filtered_words.txt"
if not os.path.exists(input_file):
    print(f"Файл {input_file} не знайдено. Створюємо тестовий файл...")
    with open(input_file, "w") as f:
        f.write("Автомобіль дорога ліс весна озеро\n")
        f.write("Гори море квітка ріка галявина\n")
        f.write("Хмара сонце дощ вітер кіт пес\n")
    print(f"Файл {input_file} створено з тестовими даними.")
def count_vowels(word):
    vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
    return sum(1 for letter in word if letter in vowels)
try:
    with open(input_file, "r") as file:
        words = file.read().split()
    word_series = pd.Series(words)
    filtered_words = word_series[word_series.apply(lambda x: count_vowels(x) >= 3)]
    with open(output_file, "w") as file:
        file.write("\n".join(filtered_words))
    print(f"Результати збережено у файл {output_file}.")
    print("Слова з 3 і більше голосними звуками:")
    print(filtered_words.tolist())
except Exception as e:
    print(f"Виникла помилка: {e}")
