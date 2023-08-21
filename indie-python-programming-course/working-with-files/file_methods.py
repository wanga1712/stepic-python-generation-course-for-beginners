# Напишите функцию file_read, которая принимает имя файла, и печатает его содержимое.
# Учитывайте, что содержимое файла может быть как на русском языке, так и на английском

# def file_read(file_name: str) -> None:
#     with open(file_name, 'r', encoding='utf-8') as file:
#         contents = file.read()
#         print(contents)

# Напишите функцию file_n_lines, которая печатает первые n-строка файла.
# Функция file_n_lines принимает на вход название файла и количество строк для прочтения.
# Не забывайте избавляться от символа переноса строки
# К примеру, если бы имелся файл hello.txt со следующим содержимым:
#
# h
# he
# hel
# hell
# hello
# То вызов file_n_lines(hello.txt, 3) должен распечатать следующее:
#
# h
# he
# hel
# Ваша задача написать только определение функции file_n_lines

# def file_n_lines(file_name: str, n: int) -> None:
#     """
#     Prints the first n lines of a file.
#
#     Args:
#         file_name (str): The name of the file.
#         n (int): The number of lines to read.
#
#     Returns:
#         None
#     """
#     with open(file_name, 'r', encoding='utf-8') as file:
#         for _ in range(n):
#             line = file.readline().rstrip()  # Read a line from the file and remove the trailing newline character
#             if not line:  # Break the loop if there are no more lines
#                 break
#             print(line)  # Print the line

# Напишите функцию create_file_with_numbers, которая принимает на вход одно целое положительное число - n.
# Функция должна создать файл с названием "range_<number>.txt" и наполнить его целыми числами от 1 до n включительно,
# причем каждое число записывается в отдельной строке
# Пример: функция create_file_with_numbers(5) должна создать файл range_5.txt с содержимым
#
# 1
# 2
# 3
# 4
# 5

# def create_file_with_numbers(n: int):
#     file_name = f'range_{n}.txt'
#     with open(file_name, 'w', encoding='utf-8') as file:
#         for i in range(1, n + 1):
#             file.write(str(i) + '\n')
#
#
# n = int(input())
# create_file_with_numbers(number_name_file)

# Напишите функцию longest_word_in_file,
# которая принимает имя файла и внутри его содержимого находит самое длинное слово
# и возвращает его в качестве ответа. В случае,  если есть несколько слов с максимальной длиной,
# нужно вернуть слово, которое встречается последнее в тексте.
# При этом слова в тексте отделяются друг от друга пробелами,
# любые другие знаки пунктуации необходимо исключить.
# И также учитывайте, что слова в тестах будут как на русском языке, так и на английском.
# Если бы содержимое файла было таким:
# He was running, but it was like running through deep water.
# There were trees all around him,
# trees which tried to stop him. They reached out with their branches.
# And it was behind him. It was coming nearer.
# то ответом было бы слово branches
# Все возможные знаки пунктуации можно получить из модуля string


# def longest_word_in_file(file_name: str):
#     from string import punctuation
#
#     longest_word = ''
#     with open(file_name, 'r', encoding='utf-8') as file:
#         contents = file.read()
#
#         # Remove all punctuation marks from the string
#         contents_cleaned = ''.join(char for char in contents if char not in punctuation)
#
#         words = contents_cleaned.split()
#         current_word = ''
#         for word in words:
#             # Check if the word is longer or equal to the current longest word
#             if len(word) >= len(longest_word):
#                 longest_word = word
#
#     return longest_word
#
# file_name = 'test.tst'
# result = longest_word_in_file(file_name)
# print(result)
from pathlib import Path

# file_path = r'C:\Users\wangr\Downloads\numbers.txt'
# count = 0
# sum_two_digit = 0
# with open(file_path, 'r', encoding='utf-8') as file:
#     for line in file:
#         cleaned_line = line.strip()
#         if len(cleaned_line.strip()) == 3:
#             count += 1
#         elif len(cleaned_line) == 2:
#             sum_two_digit += int(line)
#
# print(f'{count}\n{sum_two_digit}')

# Напишите функцию find_lines_len_more_6,
# которая принимает имя файла и находит количество строк,
# превышающее 6 символов.
# Не забывайте исключать знак переноса на новую строку, стоящий в конце строки.
# Функция find_lines_len_more_6 должна возвращать найденное количество строк
# Ваша задача написать только определение функции find_lines_len_more_6


# def find_lines_len_more_6():
#     file_path = r'C:\Users\wangr\Downloads\numbers.txt'
#     count_lines = 0
#     with open(file_path, 'r', encoding='utf-8') as file:
#         for line in file:
#             cleaned_line = line.strip()
#             if len(cleaned_line.strip()) >= 6:
#                 count_lines += 1
#     return count_lines
#
#
# lines_six = find_lines_len_more_6()
# print(lines_six)

# В вашем распоряжении имеется следующий файл.
# Ваша задача скачать его и найти сколько уникальных слов используется в этом тексте,
# при этом регистр букв не нужно учитывать.
# Это значит, что слова Lorem и loRem являются эквивалентными.
# Например, если перед вами был бы такой текст:
# Привет как дела
# привет хорошо
# то здесь четыре уникальных слова.
# Между словами в файле стоят только пробелы и переносы строк, других разделителей нет.
# В качестве ответа укажите количество уникальных слов


# def find_lines_len_more_6():
#     file_name = r'C:\Users\wangr\Downloads\lorem.txt'
#     mas = []
#     mas_set = set()
#     with open(file_name, 'r', encoding='utf-8') as file:
#         for line in file:
#             cleaned_line = line.strip().lower()
#             mas.append(cleaned_line.split())
#         for word in mas:
#             for _ in word:
#                 mas_set.add(_)
#     return len(mas_set)
#
#
# lines_six = find_lines_len_more_6()
# print(lines_six)

# def count_unique_words():
#     file_name = r'C:\Users\wangr\Downloads\lorem.txt'
#     unique_words = set()
#
#     with open(file_name, 'r', encoding='utf-8') as file:
#         for line in file:
#             words = line.strip().lower().split()
#             unique_words.update(words)  # Add words to the set using update()
#
#     return len(unique_words)
#
#
# # Call the function and print the result
# num_unique_words = count_unique_words()
# print("Number of unique words:", num_unique_words)

# В вашем распоряжении имеется файл lorem.txt.
# Ваша задача посчитать сколько раз встретилось каждое слово в этом тексте.
# Для этого создайте словарь words, где ключом будет слово,
# а значением - количество раз появления этого слова в тексте.
# Регистр букв в словах учитывать не нужно,
# поэтому слова Hello и hEllO являются эквивалентными.
# Значения ключа в словаре words записывайте в верхнем регистре
# Например, если перед вами был бы такой текст:
# Привет как дела
# привет хорошо
# то словарь words выглядел бы так
# {'ПРИВЕТ': 2, 'КАК': 1, 'ДЕЛА': 1, 'ХОРОШО': 1}
# Между словами в файле стоят только пробелы и переносы строк,
# других разделителей нет. Сам файл вы можете скачать здесь
# Ваша задача только создать переменную-словарь words и подсчитать в нем количество повторений слов.
# Выводить ничего не нужно

# def count_words():
#     words = {}
#
#     with open(file_name, 'r', encoding='utf-8') as file:
#         content = file.read()
#         words_clean = content.upper().split()
#         for word in words_clean:
#             cleaned_word = word.replace(' ', '')
#             if cleaned_word:
#                 words[cleaned_word] = words.get(cleaned_word, 0) + 1
#
#     return words

# # Call the function and print the result
# file_name = r'C:\Users\wangr\Downloads\lorem.txt'
# result = count_words()
# print(result)


# Шея, фея, затея ...
#
# В этой задаче вам необходимо обработать файл с названием words.txt,
# содержащий множество неуникальных слов.
# Само содержимое файла можно посмотреть здесь.
# Ваша задача найти в нем все слова, заканчивающиеся на строку ЕЯ, и вывести их на экран.
# При этом нужно:
#
# исключить дубли
# привести все буквы к верхнему регистру
# расположить слова в выводе в порядке двойной сортировки:
# сперва отсортировать по возрастанию длины слова, а при одинаковых значениях длины расположить по алфавиту
# Значит, если бы перед вам был файл с содержимым:
#
# панацея
# газосварщик
# ФЕЯ
# затея
# лапочка
# Гея
# панацея
# богая
# ливрея
# ШЕЯ
# я
# Камыш
# то ответ должен быть таким:
#
# ГЕЯ
# ФЕЯ
# ШЕЯ
# ЗАТЕЯ
# ЛИВРЕЯ
# ПАНАЦЕЯ
# Не забывайте про кодировку)

# def unique_words():
#     mas = []
#     mas_set = set()
#     with open(file_name, 'r', encoding='utf-8') as file:
#         for line in file:
#             cleaned_line = line.strip().upper()
#             mas.append(cleaned_line)
#         for _ in mas:
#             if _.endswith('ЕЯ'):
#                 mas_set.add(_)
#         mas_sorted = sorted(mas_set, key=lambda word: (len(word), word))
#         return mas_sorted
