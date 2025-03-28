import os

Folder_To_Find = "../A Cold Love Story Remake/game/video"
Script = "../A Cold Love Story Remake/game/script.rpy"

# Сначала получаем список MP4 файлов
files = [f for f in os.listdir(Folder_To_Find)]

# Затем читаем скрипт и ищем упоминания
with open(Script, 'r', encoding='utf-8') as file:
    relevant_lines = [line for line in file]

# Проверяем каждый файл
for filename in files:
    found = any(filename in line for line in relevant_lines)
    print(f'"{filename}" {"+" if found else "-"}') if not found else print()