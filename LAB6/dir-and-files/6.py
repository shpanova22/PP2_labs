import os
from string import ascii_uppercase  # A-Z

path = r'C:\Users\Lenovo\OneDrive\Documents\PP2_labs\LAB6'  # Папка для файлов

for char in ascii_uppercase:  # Перебираем A-Z
    file_path = os.path.join(path, f"{char}.txt")  # Создаём путь к файлу

    with open(file_path, 'x') as file:  # 'x' - создать новый файл
            print(f"Создан: {file_path}")  # Уведомление о создании файла