# Files:
# - dialogue.txt
# - Translated_Dialogue.txt
# - Output.txt
# (Coded By RootTool)

import os

def combine_files_line_by_line(file1_path, file2_path, output_path='output.txt'):
    existing_originals = set()

    with open(file1_path, 'r', encoding='utf-8') as f1, \
            open(file2_path, 'r', encoding='utf-8') as f2, \
            open(output_path, 'w', encoding='utf-8') as out:

        lines1 = [line.strip().replace('"', "'") for line in f1.readlines()]
        lines2 = [line.strip().replace('"', "'") for line in f2.readlines()]

        max_lines = max(len(lines1), len(lines2))

        for i in range(max_lines):
            line1 = lines1[i] if i < len(lines1) else ''

            if not line1 or line1 in existing_originals:
                continue

            existing_originals.add(line1)
            line2 = lines2[i] if i < len(lines2) else ''

            out.write(f'    old "{line1}"\n    new "{line2}"\n\n')

    print(f"Результат сохранён в файл: {output_path}")

def prepend_text(filename, text_to_add):
    with open(filename, 'r+', encoding='utf-8') as file:
        content = file.read()
        file.seek(0, 0)
        file.write(text_to_add + '\n' + content)
    print("Готово!")

file1 = 'dialogue.txt'
file2 = 'Translated_Dialogue.txt'
fileOut = 'Output.txt'
combine_files_line_by_line(file1, file2, fileOut)
prepend_text(fileOut, 'translate russian strings:')

def remove_empty_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    non_empty_lines = [line for line in lines if line.strip()]

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(non_empty_lines)
    print('Готово!')

#remove_empty_lines('Translated_Dialogue.txt')

def split_file(input_file, lines_per_file=10, output_dir="split_files"):
    os.makedirs(output_dir, exist_ok=True)

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    total_files = (len(lines) + lines_per_file - 1) // lines_per_file

    for i in range(total_files):
        start_idx = i * lines_per_file
        end_idx = start_idx + lines_per_file
        chunk = lines[start_idx:end_idx]

        output_file = os.path.join(output_dir, f"part_{i + 1}.txt")

        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(chunk)

    print(f"Файл разбит на {total_files} частей по {lines_per_file} строк в папке '{output_dir}'")

#split_file('dialogue.txt', 150)
