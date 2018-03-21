import sys
import os
import collections


def get_all_files(dir_path):
    files_locations = collections.defaultdict(list)
    for root, dirs, file_names in os.walk(dir_path):
        for file_name in file_names:
            file_size = os.path.getsize(os.path.join(root, file_name))
            files_locations[(file_name, file_size)].append(root)

    return files_locations


def get_duplicate_files(all_files):
    duplicate_files = {}
    for (file_name, file_size), file_root in all_files.items():
        if len(file_root) > 1:
            duplicate_files[file_name] = file_root

    return duplicate_files


def print_duplicates(duplicate_files):
    if duplicate_files:
        print('Количество дублируемых файлов — {}'.format(len(duplicate_files)))
        for file_name, file_paths in duplicate_files.items():
            print('Файл "{}" дублируется в каталогах: \n{}\n'.format(
                file_name,
                '\n'.join(file_paths)
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
