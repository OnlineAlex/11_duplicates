import sys
import os
import collections


def get_all_files(start_folder):
    all_files = collections.defaultdict(list)
    for root, dirs, name_files in os.walk(start_folder):
        for name_file in name_files:
            file_size = os.path.getsize(os.path.join(root, name_file))
            all_files[(name_file, file_size)].append(root)

    return all_files


def get_duplicate_files(all_files):
    duplicate_files = collections.defaultdict(list)
    for (file_name, file_size), file_root in all_files.items():
        if len(file_root) > 1:
            duplicate_files[file_name] = file_root

    return duplicate_files


def print_duplicates(files_data):
    if files_data:
        print('Количество дублируемых файлов — {}'.format(len(files_data)))
        for file_name, file_roots in files_data.items():
            print('Файл "{}" дублируется в каталогах: \n{}\n'.format(
                file_name,
                '\n'.join(file_roots)
            ))
    else:
        print('Дубликаты не найдены!')


if __name__ == '__main__':
    try:
        folder_path = sys.argv[1]
    except IndexError:
        exit('Укажите путь к файлу')

    if os.path.isdir(folder_path):
        folder_files = get_all_files(folder_path)
        folder_duplicate_files = get_duplicate_files(folder_files)
        print_duplicates(folder_duplicate_files)
    else:
        print('Такой папки не существует')
