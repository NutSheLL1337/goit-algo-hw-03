import os
import shutil
from pathlib import Path
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Копіювання та сортування файлів за розширенням")
    parser.add_argument('src_dir', type=str, help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням "dist")')
    args = parser.parse_args()
    return Path(args.src_dir), Path(args.dest_dir)

# Рекурсивне копіювання файлів
def parse_folder(src_path, dest_path):
    try:
        for element in src_path.iterdir():
            if element.is_dir():
                print(f"Parse folder: Це папка - {element.name}")
                parse_folder(element, dest_path)
            elif element.is_file():
                print(f"Parse folder: Це файл - {element.name}")
                copy_file(element, dest_path)
    except Exception as e:
        print(f"Помилка доступу: {e}")

# Копіювання файлу до директорії призначення
def copy_file(file_path, dest_path):
    try:
        # Отримуємо розширення файлу
        file_ext = file_path.suffix[1:]  # Видаляємо крапку
        # Створюємо папку за розширенням файлу, якщо вона не існує
        ext_folder = dest_path / file_ext
        ext_folder.mkdir(parents=True, exist_ok=True)
        # Копіюємо файл у відповідну підпапку
        shutil.copy(file_path, ext_folder / file_path.name)
        print(f"Файл {file_path.name} скопійовано до {ext_folder}")
    except Exception as e:
        print(f"Помилка копіювання файлу {file_path.name}: {e}")

if __name__ == "__main__":
    # Парсинг аргументів
    src_dir, dest_dir = parse_arguments()
    # Перевіряємо, чи існує директорія призначення
    dest_dir.mkdir(parents=True, exist_ok=True)
    # Рекурсивно обробляємо вихідну директорію
    parse_folder(src_dir, dest_dir)

        