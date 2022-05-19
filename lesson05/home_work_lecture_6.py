from functools import reduce


def is_even(a):
    """
    Принимает один аргумент
    Возвращает True - если он четный
    Возвращает False - если не четный
    """
    if a % 2 == 0:
        return True
    else:
        return False

assert is_even(1) is False
assert is_even(10) is True


def is_odd(odd_num):
    """
    Принимает один аргумент
    Использует функцию is_even из глобальной области видимости
    Внути нельзя использовать if/else
    Возвращает False - если он четный
    Возвращает True - если не четный
    """
    global is_even
    return not is_even(odd_num)

assert is_odd(2) is False
assert is_odd(11) is True


def custom_max(aa, bb):
    """
    Принимает два аргумента
    Не использовать фнукцию max внути
    Возвращает наибольший из двух элементов
    """
    if aa > bb:
        return aa
    else:
        return bb

assert custom_max(1, 10) == max(1, 10)
assert custom_max(100, 10) == max(100, 10)


def multiply(*kwargs, base=1):
    """
    Принимает любое кол-во аргументов и один дополнительный необязательный именованный аргумент base
    base по умолчанию равен 1
    Возвращает результат перемножения всех переданных аргументов и необязательного
    """
    return reduce(lambda total, val: total * val, kwargs) * base


example_list = list(range(1, 10))

assert multiply(*example_list) == 362880
assert multiply(*example_list, base=2) == 725760


def custom_reverse(string_to_reverse: str):
    """
    Принимает один аргумент, строку
    Возвращает развернутую строку
    """
    return string_to_reverse[::-1]

assert custom_reverse("") == ""
assert custom_reverse("QWERqwer123!@#") == "#@!321rewqREWQ"


def upper_count(str_to_count_upper: str):
    """
    Принимает один агрумент, строку
    Возвращает кол-во букв в верхнем регистре
    """
    count = 0
    for letter in str_to_count_upper:
        if letter.isupper():
            count += 1
    return count

assert upper_count("") == 0
assert upper_count("QWER qwer 123 !@#") == 4


def unique(list_to_process: list):
    """
    Принмает один аргумент, список
    Возвращает список уникальных элементов этого списка отсортированных от меньшего к большему
    """
    sorted_list_unique = list(set(sorted(list_to_process)))
    return sorted_list_unique

assert unique([2, 2, 1, 5, 5, 2, 7]) == [1, 2, 5, 7]


def is_pangram(alphabet_str:str):
    """
    Функция принимает один аргумент, строку
    Возвращает True если в строке хотя бы раз встречается каждая буква английского алфавита
    иначе возвращает False
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_dict = {char: 0 for char in alphabet}
    for char in alphabet_str.lower().replace(" ", ""):
        if char not in alphabet_dict:
            continue
        else:
            alphabet_dict[char] += 1

    found_zero = False
    for v in alphabet_dict:
        if v is False:
            found_zero = True
            break

    if found_zero:
        return False
    else:
        return True

assert is_pangram("The five boxing wizards jump quickly") is True
