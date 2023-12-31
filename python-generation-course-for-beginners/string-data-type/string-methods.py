# Количество слов
# На вход программе подается строка текста,
# состоящая из слов, разделенных ровно одним пробелом.
# Напишите программу, которая подсчитывает количество слов в ней.
# Формат входных данных
# На вход программе подается строка текста.
# Формат выходных данных
# Программа должна вывести количество слов.
# Примечание 1. Строка текста не содержит пробелов в начале и конце.
# Примечание 2. Используйте для решения задачи метод count.

# string = input()
# symbol_for_counting = ' '
# print(string.count(symbol_for_counting) + 1)

# Минутка генетики
# На вход программе подается строка генетического кода,
# состоящая из букв А (аденин), Г (гуанин), Ц (цитозин), Т (тимин).
# Напишите программу, которая подсчитывает сколько аденина, гуанина,
# цитозина и тимина входит в данную строку генетического кода.
# Формат входных данных
# На вход программе подается строка генетического кода, состоящая из символов А, Г, Ц, Т, а, г, ц, т.
# Формат выходных данных
# Программа должна вывести сколько гуанина, тимина, цитозина, аденина входит в данную строку генетического кода.
# Примечание. Строка не содержит символов, кроме как А, Г, Ц, Т, а, г, ц, т.

# string = input().upper()
# adenine, guanine, cytosine, thymine = 'А', 'Г', 'Ц', 'Т'
# print(f'Аденин: {string.count(adenine)}\nГуанин: {string.count(guanine)}\n\
# Цитозин: {string.count(cytosine)}\nТимин: {string.count(thymine)}')

# Очень странные дела
# Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди. На приемник ему поступает n
# различных последовательностей кода Морзе.
# Декодировав их, он получает последовательности из цифр
# и строчного латинского алфавита, при этом во всех сообщениях
# Оди содержится число 11, причем минимум 3 раза.
# Помогите определить Джиму количество сообщений от Оди.
# Формат входных данных
# В первой строке подаётся число
# n – количество сообщений, в последующих
# n строках вводятся строки, содержащие латинские строчные буквы и цифры.
# Формат выходных данных
# Программа должна вывести количество строк в которых содержится число 11 минимум 3 раза.
# Примечание: Числа 11 необязательно должны быть разделены другими символами,
# нужно подсчитать вхождение последовательности символов "11",
# т.е. например в строке "111" содержится одна такая последовательность,
# в то время как в "1111" их уже две.

# numbers_of_messages = int(input())
# count = 0
# for i in range(numbers_of_messages):
#     string = input()
#     if string.count('11') >= 3:
#         count += 1
# print(count)

# Количество цифр
# На вход программе подается строка текста.
# Напишите программу, которая подсчитывает количество цифр в данной строке.
# Формат входных данных
# На вход программе подается строка текста.
# Формат выходных данных
# Программа должна вывести количество цифр в данной строке.

# string = input()
# count = 0
# for i in string:
#     if i.isdigit():
#         count += 1
# print(count)

# .com or .ru
# На вход программе подается строка текста.
# Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.
# Формат входных данных
# На вход программе подается строка текста.
# Формат выходных данных
# Программа должна вывести «YES» если введенная строка заканчивается подстрокой
# .com или .ru и «NO» в противном случае.

# string = input()
# if string.endswith('.com') or string.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')

# Самый частотный символ
# На вход программе подается строка текста.
# Напишите программу, которая выводит на экран символ, который появляется наиболее часто.
# Формат входных данных
# На вход программе подается строка текста.
# Текст может содержать строчные и заглавные буквы английского и русского алфавита, а также цифры.
# Формат выходных данных
# Программа должна вывести символ, который появляется наиболее часто.
# Примечание 1. Если таких символов несколько, следует вывести последний по порядку символ.
# Примечание 2. Следует различать заглавные и строчные буквы, а также буквы русского и английского алфавита.

# string = input()
# chek_letter = ''
# number_letter = 0
# for letter in string:
#     if number_letter <= string.count(letter):
#         number_letter = string.count(letter)
#         chek_letter = letter
# print(chek_letter)

# Первое и последнее вхождение
# На вход программе подается строка текста.
# Если в этой строке буква «f» встречается только один раз, выведите её индекс.
# Если она встречается два и более раз, выведите индекс её первого и последнего
# вхождения на одной строке, разделенных символом пробела.
# Если буква «f» в данной строке не встречается, следует вывести «NO».
# Формат входных данных
# На вход программе подается строка текста.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# string = input()
# left_count_index = string.find('f')
# right_count_index = string.rfind('f')
# if left_count_index == -1:
#     print('NO')
# elif string.count('f') >= 2:
#     print(left_count_index, right_count_index)
# else:
#     print(left_count_index)


# Удаление фрагмента
# На вход программе подается строка текста,
# в которой буква «h» встречается минимум два раза.
# Напишите программу, которая удаляет из этой строки первое и последнее вхождение
# буквы «h», а также все символы, находящиеся между ними.
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# string = input()
# left_find_index = string.find('h')
# right_find_index = string.rfind('h')
# print(f'{string[:left_find_index]}{string[right_find_index + 1:]}')

# if left_count_index == -1:
#     print('NO')
# elif string.count('f') >= 2:
#     print(left_count_index, right_count_index)
# else:
#     print(left_count_index)

# Символы в диапазоне
# На вход программе подаются два числа
# a и b. Напишите программу, которая для каждого кодового значения в диапазоне от
# a до b (включительно), выводит соответствующий ему символ из таблицы символов Unicode.
# Формат входных данных
# На вход программе подается два натуральных числа, каждое на отдельное строке.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# numbers = []
# for i in range(2):
#     number = int(input())
#     numbers.append(number)
# for i in range(numbers[0], numbers[1] + 1):
#     print(f'{chr(i)}', end=' ')

# Простой шифр
# На вход программе подается строка текста.
# Напишите программу, которая переводит каждый ее символ в соответствующий
# ему код из таблицы символов Unicode.
# Формат входных данных
# На вход программе подается строка текста.
# Формат выходных данных
# Программа должна вывести кодовые значения символов строки разделенных одним символом пробела.

# str = input()
# str_mas = list(str)
# for i in str_mas:
#     print(ord(i), end=' ')


# Шифр Цезаря 🌶️ Легион
# Цезаря, созданный вn 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр
# Цезаря.Это их и подвело, ведь данный шифр очень простой.
# Однако в постапокалипсисе люди плохо знают все тонкости довоенного мира,
# поэтому ученые из НКР не могут понять, как именно нужно декодировать данные сообщения.
# Напишите программу для декодирования этого шифра.
#  Формат входных данных В первой строке дается число
# (1 ≤ 25)
# n(1≤ n≤ 25) – сдвиг, во второй строке даётся закодированное
# сообщение в виде строки со строчными латинскими буквами.
#  Формат выходных данных Программа должна вывести одну строку
# – декодированное сообщение.
# Обратите внимание, что нужно декодировать сообщение, а не закодировать.

# shit = int(input())
# encoding_word = list(input())
# decoded_word = []
# for i in encoding_word:
#     decoded_char = ord(i) - shit
#     if decoded_char < 97:
#         decoded_char = 122 - (96 - decoded_char)
#         decoded_word.append(chr(decoded_char))
#     else:
#         decoded_word.append(chr(decoded_char))
# print(*decoded_word, sep='')