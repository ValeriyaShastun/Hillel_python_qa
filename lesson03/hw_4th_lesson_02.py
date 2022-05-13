# Задача 1
#
# Пользователь вводит одно число - любое значение которое гарантированное можно
# перевести в int. Определить его кратность 2, 3, 5, 7 или самому себе. Вывести
# строку f"multiple of {val}" где val - значение кратности. Если число кратно
# нескольким значениям - выводить только наименьшее. Не используйте циклы в этой
# задаче. Используйте конструкцию if/elif/.../elif/else для того что бы проверить
# каждый из вариантов кратности.

user_input = int(input('Please insert any number'))
list_to_check_1 = [2, 3, 5, 7]
list_to_check_1.append(user_input)
if user_input % user_input == 0 and user_input < list_to_check_1[0]:
    print(f"multiple of {user_input}")
elif user_input % list_to_check_1[0] == 0:
    print(f"multiple of {list_to_check_1[0]}")
elif user_input % list_to_check_1[1] == 0:
    print(f"multiple of {list_to_check_1[1]}")
elif user_input % list_to_check_1[2] == 0:
    print(f"multiple of {list_to_check_1[2]}")
elif user_input % list_to_check_1[3] == 0:
    print(f"multiple of {list_to_check_1[3]}")
elif user_input % user_input == 0:
    print(f"multiple of {user_input}")
else:
    print(f'{user_input} is not multiple of any number in sequence')

# Задача 2
#
# Пользователь вводит стоп слово - это может быть набор букв и цифр без пробелов и знаков препинания.
# Используйте цикл, и input что бы заполнить список вводом от пользователя. На каждой итерации пользователь
# будет вводить строку состоящую из символов букв, цифр, пробелов и знаков препинания. Добавляйте этот ввод
# в список. Если во вводе пользователя есть стоп слово, но ввод целиком не равен ему - перед добавлением в
# список удалите стоп слово из строки ввода.
#
# Как только пользователь введет стоп слово - прервите цикл и выведете все что вводил пользователь. Для
# прерывания цикла строка должна быть строго равна стоп слову.
# Вывод скрипта гарантированно не должен содержать в себе стоп слово. Выводите каждый ввод на отдельной
# строке. Не добавляйте в вывод скрипта ничего сверх того что вводил пользователь (порядковый номер ввода,
# разделители и т.д.).
# Ограничьте количество итераций максимум 30. Пользователь вводит стоп слово (начало скрипта), и затем может
# максимум 30 раз произвести ввод. После 30 раза итерация должна быть прервана.
#
# Ограничьте количество итераций минимум 5. Пользователь вводит стоп слово (начало скрипта), первые 5 итераций не
# будут прерваны если пользователь будет вводить стоп слово. Если пользователь введет стоп слово в первых 5
# итерациях - оно не будет добавлено в список.

stop_word = input('PLease enter stop-word and hit [Enter]')
list_to_append2 = []
index = 0
while index in range(30):
    user_input_2 = input('Please enter letters or numbers without spaces and punctuation marks')
    if stop_word == user_input_2 and index >= 5:
        break
    elif stop_word in user_input_2:
        datum_to_append = user_input_2.replace(stop_word, '')
        if datum_to_append == '':
            index += 1
            continue
        list_to_append2.append(datum_to_append)
    else:
        list_to_append2.append(user_input_2)
    index += 1
print(list_to_append2)

# Задача 3
#
# Пользователь вводит ключи словаря через пробел (это всегда будут буквы и цифры разделенные
# пробелом). Затем пользователь вводит значения словаря через пробел (это всегда будут буквы
# и цифры разделенные пробелом). Создать из пользовательского ввода словарь, где введенные
# ключи будут соответствовать введенным значениям. Гарантированно, что количество ключей и
# значений одинаково и больше нуля.
# Используйте enumerate для итерации по ключам или значениям при заполнении/создании словаря.
# Используйте zip для итерации по ключам или значениям при заполнении/создании словаря.

keys_str = input("Please enter keys to the dictionary separated by space and hit [Enter]")
keys_list = keys_str.split()
keys_val = input("Please enter values to the dictionary separated by space and hit [Enter]")
val_list = keys_val.split()
dict_to_fill = {}
if len(keys_list) > 0 and len(val_list) > 0:
    for i, k in enumerate(keys_list):
        dict_to_fill.update({k: val_list[i]})
    print(dict_to_fill)

    for k, v in zip(keys_list, val_list):
        dict_to_fill.update({k: v})
    print(dict_to_fill)

    dict_to_fill_1 = {key: value for key, value in zip(keys_list, val_list)}
    print(dict_to_fill)
else:
    print('Please enter keys and values!')

# Задача 4
#
# Пользователь вводит число. Используя list comprehension создать список кубов всех чисел от
# нуля до числа пользователя (не включая его), если текущее число минус 1 (число текущей
# итерации для которого считается куб) кратно 3.

user_input_4 = int(input('PLease enter a number and hit [Enter]'))
list_of_3d_grade = [num ** 3 for num in range(user_input_4) if (num - 1) % 3 == 0 ]
print(list_of_3d_grade)

# Задача 5
#
# Пользователь вводит числа разделенные пробелом. Преобразовать ввод пользователя в список
# используя .split(). Используя конструкцию if/elif/.../elif/else вывести:
# Если в списке нет значений - вывести "Empty".
# Если же в списке встречается хотя бы одна строка "5" - посчитайте количество символов "5"
# в пользовательском вводе (не в списке) и умножьте str("5") на это значение. Выведете
# получившуюся строку.
# Если же в списке только одно значение - возведите его в квадрат предварительно переведя в
# int
# Если же в списке четное кол-во элементов - используя методы max и min найдите максимальное
# и минимальное значение в списке, переведите их в int и выведете их произведение. При этом
# max и min будут возвращать максимальное и минимальное строковое значение из списка, а не
# максимальное и минимальное цифровое значение.
# Во всех остальных случаях вывести только уникальные элементы списка разделенные запятой.
# Не используйте циклы.
# Ввод пользователя может быть пустым.

user_input_5 = input('Please enter numbers separated by space and hit [Enter]')
user_input_5_list = user_input_5.split()
if user_input_5_list == []:
    print('Empty')
elif "5" in user_input_5_list:
    number_of_occurances_5 = user_input_5.count("5")
    print("5" * number_of_occurances_5)
elif len(user_input_5_list) == 1:
    print(int(user_input_5_list[0]) ** 2)
elif len(user_input_5_list) % 2 == 0:
    print(int(min(user_input_5_list)) * int(max(user_input_5_list)))
else:
    print(set(user_input_5_list))
