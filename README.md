# Анти дубликатор
Скрип ищет дубликаты файлов в указанной папке и ее подпапках. Если такие файлы найдены вы получите их список. 

# Как работает 
```bash
$ python duplicates.py /home/Myhome/github/
Количество дублируемых файлов — 26
Файл "README.md" дублируется в каталогах: 
A:\test_git
A:\test_git\4_project                        

Файл "config" дублируется в каталогах: 
A:\test_git\3_project\.git
A:\test_git\4_project\.git       
```
# Требования
Совестимые OC:
* Linux,
* Windows
* MacOS
Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 выше
# Как запустить
Скрипт запускается стандатной командой `python` (на некоторых компьютерах `python3`)

Затем напишите название файла `duplicates.py` и передайте путь к папке с которой начать анализ — С:\StartFolder\

> Запуск для всех ОС одинаковый
```bash
$ python duplicates.py <путь к папке>
```
# Цели проекта
Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)