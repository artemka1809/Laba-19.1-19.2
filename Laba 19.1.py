import pandas as pd
import os
filename = "input.csv"
if not os.path.exists(filename):
    print(f"Файл {filename} не знайдено. Створюємо тестовий файл...")
    with open(filename, "w") as f:
        f.write("Firm1,Firm2,Firm3\n")
        f.write("120,150,130\n")
        f.write("110,160,140\n")
        f.write("130,140,150\n")
    print(f"Файл {filename} створено з тестовими даними.")
try:
    df = pd.read_csv(filename)
    print("Вміст файлу:")
    print(df)
    totals = df.sum()
    print("\nЗагальна кількість виготовлених покришок для кожної фірми:")
    print(totals)
    totals.to_csv("output.csv", header=["Total"], index_label="Firm")
    print("\nРезультати збережено у файл output.csv.")
except Exception as e:
    print(f"Виникла помилка: {e}")
