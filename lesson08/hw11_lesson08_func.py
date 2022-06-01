def is_even(a):
    """
    Принимает один аргумент
    Возвращает True - если он четный
    Возвращает False - если не четный
    """
    if type(a) is not int:
        raise TypeError
    return True if a % 2 == 0 else False


def is_odd(odd_num):
    """
    Принимает один аргумент
    Использует функцию is_even из глобальной области видимости
    Внути нельзя использовать if/else
    Возвращает False - если он четный
    Возвращает True - если не четный
    """
    num_to_process = int(odd_num)
    return not is_even(num_to_process)


def custom_max(aa, bb):
    """
    Принимает два аргумента
    Не использовать фнукцию max внути
    Возвращает наибольший из двух элементов
    """
    first_num = int(aa)
    second_num = int(bb)
    return first_num if first_num > second_num else second_num


def multiply(*kwargs, base=1):
    """
    Принимает любое кол-во аргументов и один дополнительный необязательный именованный аргумент base
    base по умолчанию равен 1
    Возвращает результат перемножения всех переданных аргументов и необязательного
    """
    num_to_remember = 1
    for num in kwargs:
        result = num * num_to_remember
        num_to_remember = result
    return num_to_remember * base


def custom_reverse(string_to_reverse: str):
    """
    Принимает один аргумент, строку
    Возвращает развернутую строку
    """
    return string_to_reverse[::-1]


def upper_count(str_to_count_upper: str):
    """
    Принимает один агрумент, строку
    Возвращает кол-во букв в верхнем регистре
    """

    list_to_check = [letter.isupper() for letter in str_to_count_upper]
    count = sum(list_to_check)
    return count


def unique(list_to_process: list):
    """
    Принмает один аргумент, список
    Возвращает список уникальных элементов этого списка отсортированных от меньшего к большему
    """
    return list(set(sorted(list_to_process)))


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
    for k in alphabet_dict:
        if alphabet_dict.get(k) == 0:
            found_zero = True
            break

    if found_zero:
        return False
    else:
        return True

assert is_pangram("I love python") is False