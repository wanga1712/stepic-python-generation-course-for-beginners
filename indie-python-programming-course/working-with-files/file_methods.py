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
# Функция должна создать файл с название "range_<number>.txt" и наполнить его целыми числами от 1 до n включительно,
# причем каждое число записывается  в отдельной строке
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