import os

def check_files_in_directory(directory_path, txt_file_path):
    """
    Проверяет наличие имен файлов из каталога в текстовом файле
    
    :param directory_path: путь к каталогу с файлами
    :param txt_file_path: путь к текстовому файлу для проверки
    """
    # Читаем содержимое текстового файла
    with open(txt_file_path, 'r', encoding='utf-8') as f:
        txt_content = f.read()

    not_founded = 0
    for filename in os.listdir(directory_path):
        if filename in txt_content:
            #print(f"[+] '{filename}'")
            pass
        else:
            print(f"[-] '{filename}'")
            not_founded += 1
                
    print(f"Not Founded: {not_founded}")

# Пример использования
if __name__ == "__main__":
    #directory_to_scan = r'C:\Users\RootTool\Documents\GitHub\Clones\ACLS_DEV\A Cold Love Story Remake\game\video'
    directory_to_scan = r'C:\Users\RootTool\Documents\GitHub\Clones\ACLS_DEV\A Cold Love Story Remake\game\audio'
    text_file_to_check = r'C:\Users\RootTool\Documents\GitHub\Clones\ACLS_DEV\A Cold Love Story Remake\game\script.rpy'
    
    check_files_in_directory(directory_to_scan, text_file_to_check)
