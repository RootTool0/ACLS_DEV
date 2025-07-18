# Объединяет русский и англ. файлы переводов в локализацию для RenPy
# Input:
# @param Russian.txt
# @param English.txt
# Output:
# @param Output.txt
# (Coded By RootTool)

import os

def combine_files_line_by_line(RussianFile, EnglishFile, OutputFile='output.txt'):
    ExistingEnglishLines = set()

    with open(RussianFile, 'r', encoding='utf-8') as RussianFileReader, \
            open(EnglishFile, 'r', encoding='utf-8') as EnglishFileReader, \
            open(OutputFile, 'w', encoding='utf-8') as OutputFileWriter:

        RussianLines = [line.strip().replace('"', "'") for line in RussianFileReader.readlines()]
        EnglishLines = [line.strip().replace('"', "'") for line in EnglishFileReader.readlines()]
        
        max_lines = max(len(RussianLines), len(EnglishLines))

        OutputFileWriter.write('translate russian strings:\n')
        for i in range(max_lines):
            EnglishLine = EnglishLines[i] if i < len(EnglishLines) else ''

            if not EnglishLine or EnglishLine in ExistingEnglishLines:
                continue

            ExistingEnglishLines.add(EnglishLine)
            RussianLine = RussianLines[i] if i < len(RussianLines) else ''

            OutputFileWriter.write(f'    old "{EnglishLine}"\n    new "{RussianLine}"\n\n')

    print(f"Результат сохранён в файл: {OutputFile}")

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

if __name__ == "__main__":
    RussianFile = 'Russian.txt'
    EnglishFile = 'English.txt'
    OutputFile = 'Output.txt'

    combine_files_line_by_line(RussianFile, EnglishFile, OutputFile)
