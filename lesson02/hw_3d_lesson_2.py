# 1. Принять пользовательский однострочный ввод. Необходимо на каждой новой строке
# - развернуть пользовательский ввод
# - заменить все вхождения "bad" на "good" в не измененном пользовательском вводе
# - сколько замен было произведено

user_str = input('Please type three things which can ge bad and press [Enter]:')
reverse_user_str = user_str[::-1]
replace_user_str = user_str.replace("bad", "good")
replace_count = replace_user_str.count("good")

# 2. Составить выражение из True, False, not, and, or которое будет состоять как
# минимум из 3 "слов". На первой строке - само выражение, на второй - это же
# выражение, в котором расставлены скобки так, что порядок выполнения не меняется.
# Например
# True and False or not False or True and False
# (((True and False) or (not False)) or (True and False))

n = False or True and False or True or not False
n_amend = (((False or (True and False)) or True) or (not False))

# 3. Есть список (в 1-й строке вашего скрипта созданный вами, я его могу
# заменить на любой другой во время проверки) из случайного кол-ва элементов
# (минимум 10). Необходимо на каждой новой строке
# - вывести последний элемент используя индексы
# - вывести последний элемент НЕ используя отрицательные индексы

list_for_task_3 = [30, 50, 789, 203, 4805, "hi_there", 8.9, (5, 4, 7, "2"),
                   None, True, False, [6, 9, 7, 2]]
length = len(list_for_task_3)
print(list_for_task_3[-1])
print(list_for_task_3[length-1])

# 4. Есть список (в 1-й строке вашего скрипта созданный вами, я его могу
# заменить на любой другой во время проверки) из случайного кол-ва элементов
# (минимум 10).
# Пользователь вводит начало, конец и шаг слайса - вывести слайс

list_for_task_4 = ["hi_teacher", 8.9, (5, 4, 7, "2"), 30, 50, 789, 203, 4805,
                   True, False, [6, 9, 7, 2], None]
start = int(input("Please enter START of the slice"))
stop = int(input("Please enter END of the slice"))
step = int(input("Please enter STEP of the slice"))
print(list_for_task_4[start:stop:step])

# 5. Есть список (в 1-й строке вашего скрипта созданный вами, я его могу
# заменить на любой другой во время проверки) из случайного кол-ва элементов
# (минимум 10). Гарантированно 3 из них имеют дубли.
# Вывести список (list) без дублей используя только преобразование типов
# данных

list_for_task_5 = ["hi_teacher", None, False, 30, 50, 789, 30, 50, 200,
                   50, False, None]
list_without_duplicates = list(set(list_for_task_5))

# 6. Пользователь два раза вводит слова через пробел (только буквы и пробел).
# Вывести только слова которые есть в обеих вводах.

input_first = input("Enter your favourite countries, separate data using "
                    "space, then press [Enter]")
input_second = input("Enter countries you've travelled to, separate data "
                     "using space, then press [Enter]")
input_first_strip = input_first.split()
input_second_strip = input_second.split()
list_without_duplicates_6 = []
for country in input_first_strip:
    if country in input_second_strip:
        list_without_duplicates_6.append(country)

print(list_without_duplicates_6)

# 7. Есть список (в 1-й строке вашего скрипта созданный вами, я его могу
# заменить на любой другой во время проверки) из случайного кол-ва
# элементов (минимум 10) который гарантированно является последовательностью
# с пропущенным значением (0 1 2 3 5 7 8 9...).
# Вывести set значений которые пропущены в списке

list_with_missin = [0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 17]
set_for_answer = set()
for i in range(18):
    if i not in list_with_missin:
        set_for_answer.add(i)

# 8. Инициализировать пустой словарь
# - Спросить имя пользователя и добавить его в словарь
# - Спросить возраст пользователя и добавить его в словарь
# - Спросить названия любимых фильмов пользователя, введенных через запятую, и добавить их в словарь списком
# - Вывести пользователю весь словарь
# - Вывести пользователю список ключей словаря
# - Спросить пользователя какой элемент заменить
# - Спросить пользователя на какую строку заменить элемент
# - Заменить указанный элемент на указанную строку
# - Вывести словарь
# - Попросить пользователя ввести ключ который может быть а может не быть в словаре
# - Запросить значение которое вывести если в словаре нет этого ключа
# - Вывести значение из словаря или пользовательское

dict_for_8 = {}
user_name = input('Please insert your name and press [Enter]')
dict_for_8.update({"Name": user_name})
user_age = input('Please insert your age and press [Enter]')
dict_for_8.update({"Age": user_age})
user_fav_movies = input('Please insert your favourite movies separated by comma and press [Enter]')
movies_list = user_fav_movies.split(",")
dict_for_8.update({"Movies": movies_list})
print(dict_for_8)
print(dict_for_8.keys())
replace_item_key = input('Please insert the name of element to replace and press [Enter]')
replace_item_value = input(f'Please insert the text to be inserted into {replace_item_key} and press [Enter]')
dict_for_8[replace_item_key] = replace_item_value
print(dict_for_8)
key_to_check = input('Please insert key name you want to check in the dictionary and press [Enter]')
value_to_check = input('Please insert key name you want to receive if there is no such a key in '
                       'the dictionary and press [Enter]')
print(dict_for_8.get(key_to_check, value_to_check))
