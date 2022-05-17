# Необходимо создать скрипт который должен:
#
# открыть файл example.txt который лежит с ним в одной папке
# если файл не существует - предотвратить ошибку и напечатать пользователю что ошибка была предотвращена, файл
# не существует и остановить работу скрипта

# вывести в консоль самое часто встречаемое слово в файле, и сколько раз оно встречается
# вывести в консоль самое редко встречаемое слово в файле, и сколько раз оно встречается
# создать файл spam.txt в который записать содержимое файла заменив самое часто встречаемое слово на самое редко встречаемое слово
# Файлы НЕ будут идентичными - единственный критерий - те же слова, в том же порядке, но с произведенной заменой
# Длинна строки - 10 слов (необязательное дополнительное задание)
# если файл уже существует - ничего не писать в него, сообщить пользователю что файл существует и остановить работу скрипта
#
# Текст может содержать буквы верхнего и нижнего регистра (в любой последовательности), точку, запятую, знак вопроса, знак восклицания.
# В нем не будет цифр, двойных пробелов, множества переносов и прочего. Так же после знаков препинания будет пробел или перенос строки.
#
# Ничего не импортировать.
#
# Функции и классы не создавать.
#
# Для сортировки можно использовать sorted
#
# example_list = [7, 2, 3, 2, 3, 1, 5, 4, 6, 2, 4]
# print(sorted(example_list, key=example_list.count))
# # [7, 1, 5, 6, 3, 3, 4, 4, 2, 2, 2]
#
# key принимает функцию, в данном случае это функция - кол-во элементов в конкретном списке example_list
# (по какуму критерию происходит сортировка)
#
# одинаковые элементы с одинаковым кол-вом повторений могут идти не подряд, это зависит от изначального порядка в списке
#
# example_list = [5, 2, 3, 2, 1, 7, 4, 6, 2, 4, 3]
# ...
# # [5, 1, 7, 6, 3, 4, 4, 3, 2, 2, 2]
#
# Если самое часто и редко встречаемое слово не одно, а например есть еще одно с таким же кол-вом повторений - правильным
# будет любое из них, но оно должно быть одинаковым во всем скрипте.

try:
    with open('example.txt', "r") as file:
        text = file.read()
    text_lower = text.lower()
    text_split = text_lower.split(' ')
    min_count = 999
    max_count = 1
    min_word = ""
    max_word = ""
    for word in text_split:
        count = text_split.count(word)
        if count <= min_count:
           min_count, min_word = count, word
        elif count >= max_count:
           max_count, max_word = count, word
    print(max_count, max_word)
    print(min_count, min_word)
    #or
    sorted_list = sorted(text_split, key=text_split.count)
    most_frequent_word = sorted_list[-1]
    print(most_frequent_word, sorted_list.count(most_frequent_word))
    most_rare_word = sorted_list[0]
    print(most_rare_word, sorted_list.count(most_rare_word))

    # replacing most frequent to most rare word:
    replaced_text_split = text_lower.replace(most_frequent_word, most_rare_word).split()
    # making line of 10 words
    text_to_write = []
    for idx, element in enumerate(replaced_text_split):
        text_to_write.append(element)
        if idx % 10 == 0 and idx > 0:
            text_to_write.append("\n")

    with open("spam.txt", "x") as spam:
        spam.write(" ".join(text_to_write))

except FileNotFoundError as e:
    print("The file example.txt doesn't exist")
except FileExistsError as err:
    print("The file spam.txt already exists")
