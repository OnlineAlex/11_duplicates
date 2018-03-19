import sys
import os
import collections


def get_all_files(start_folder):
    all_files = collections.defaultdict(list)
    for root, dirs, files in os.walk(start_folder):
        for file in files:
            file_path = os.path.join(root, file)
            all_files[file].append(os.path.getsize(file_path))

    return all_files


def get_duplicate_files(all_files):
    duplicate_files_list = []
    for file_name, file_size in all_files.items():
        if len(file_size) - len(set(file_size)):
            duplicate_files_list.append(file_name)

    return duplicate_files_list


def print_duplicates(files_list):
    if files_list:
        print('Эти файлы дублируются:\n{}'.format(', '.join(files_list)))
    else:
        print('Дубликаты не найдены!')


if __name__ == '__main__':
    try:
        folder_path = sys.argv[1]
    except IndexError:
        exit('Укажите путь к файлу')

    if os.access(folder_path, os.F_OK):
        folder_files = get_all_files(folder_path)
        duplicate_files = get_duplicate_files(folder_files)
        print_duplicates(duplicate_files)
    else:
        print('Такой папки не существует')
