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


