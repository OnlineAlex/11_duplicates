# Анти дубликатор
Скрип ищет дубликаты файлов в указанной папке и ее подпапках. Если такие файлы найдены вы получите их список. 

# Как работает 
```bash
$ python duplicates.py /home/Myhome/github/
Эти файлы дублируются:
README.md, config, description, HEAD, index, packed-refs, applypatch-msg.sample, commit-msg.sample, fsmonitor-watchman.sample
```
# Требования
Совестимые OC:
* Linux,
* Windows
* MacOS
Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 выше
# Как запустить
Скрипт запускается стандатной командой `python` (на некоторых компьютерах `python3`)

Затем напишите название файла `password_strength.py` и передайте путь к папке с которой начать анализ — С:\StartFolder\

> Запуск для всех ОС одинаковый
```bash
$ python duplicates.py <путь к папке>
```
# Цели проекта
Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)