def file_to_read_path() -> str:
    """
    Asks user for path to file to be opened
    :return path to file in str format
    """
    path_to_file = input("Please enter path to file to open")
    return path_to_file

def read_file(path_to_file: str) -> str:
    """
    Opens file on path and reads it
    :param: path_to_file starting from directory script is starting
    or absolute path
    :return file content in str format
    """
    with open(path_to_file, "r") as file:
        text = file.read()
    return text

def prepare_text(text: str) -> str:
    """
    Removes dots, colons, semicolons and comas from text
    Switches text to lowercase
    :param text: text to be processed
    :return: text without punctuation marks
    """
    text_to_return = text.lower().replace(",", "").replace(".", "").replace(":", "").replace(";", "")
    return text_to_return

def search_of_word_count(text: str, max = True) -> str:
    """
    Helps to find word in the text of particular parameter
    :param text: text to be processed
    :param max: to find the most frequent word in the text max = True
                to find the most rare word in the text max = False
    :return: the most frequent word or the most rare word
    """
    text_split = text.split(' ')
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

    if max:
        print(max_word, max_count)
        return max_word
    else:
        print(min_word, min_count)
        return min_word

def replace_frequent_to_rare(text_to_process: str, frequent_word: str, rare_word: str) -> list:
    """
    Replaces the most frequent word to the most rare word
    :param text_to_process: text where we replace most frequent word to most rare word
    :param frequent_word: the most frequent word
    :param rare_word: the most rare word
    :return: text with replaced words
    """
    # text_with_replace = text_to_process.replace(frequent_word, rare_word) # реплейс происходит в тексте, а нужно заменять слова в списке.
                                                                            # в тексте могут быть слова в которых есть подстроки которые
                                                                            # подходят для замены, хотя не должны быть заменены
    list_to_process = text_to_process.split()
    for i in range(len(list_to_process)):
        if list_to_process[i] == frequent_word:
            list_to_process[i] = rare_word
    return list_to_process

def text_with_number_of_words_in_line(list_to_process: list, number_of_words_in_line: int) -> str:
    """
    changes text to multiline text with exact count of words in line
    :param text_to_process: text we work on
    :param number_of_words_in_line: number of words in line
    :return: text with exact line length
    """
    text_to_write = []
    for idx, element in enumerate(list_to_process):
        text_to_write.append(element)
        if idx % number_of_words_in_line == 0 and idx > 0:
            text_to_write.append("\n")

    final_text = " ".join(text_to_write)
    return final_text

def write_to_file(file_name: str, text: str, flag_for_file: str = "x"):
    """
    Asks user to insert path to file in console and writes text into the file with
    user defined name
    :param text: text to write in the file
    :param file_name: file to be created with text
    :return:
    """
    # try:
    #     with open(file_name, "x") as spam:
    #         spam.write(text)
    # except FileExistsError as err:
    #     print(f"The file {file_name} already exists")
    #     resp = input("Do you want to change file? Enter Y/N")
    #     if resp == "Y" or resp == "Y".lower():   # вот тут можно использовать рекурсию, и флаг в аргументах
    #         with open(file_name, "w") as spam:     # с дефолтным значением (потому что целевая функция использует флаг)
    #             spam.write(text)                   # а в случае если нет - райсить перехваченную ошибку
    #
    try:
        with open(file_name, flag_for_file) as spam:
            spam.write(text)
    except FileExistsError as err:
        resp = input("Do you want to change file? Enter Y/N")
        if resp == "Y" or resp == "Y".lower():
            write_to_file(file_name, text, flag_for_file = "w")
        else:
            raise err

def file_to_write_path() -> str:
    """
    Asks user for path to file to write text into
    :return path to file in str format
    """
    path_to_file = input("Please enter path to file to write text in")
    return path_to_file

def main():
    """
    Это ваша главная функция, определите в ней всю лолгику скрипта и используйте другие функции которые определите ВЫШЕ
    """
    path_to_read_file = file_to_read_path()
    try:
        text_from_file = read_file(path_to_read_file)
        text_without_marks = prepare_text(text_from_file)
        min_word = search_of_word_count(text_without_marks, max = False)
        max_word = search_of_word_count(text_without_marks)
        text_replaced = replace_frequent_to_rare(text_without_marks, max_word, min_word)
        fin_text = text_with_number_of_words_in_line(text_replaced, 10)
        file_to_write_name = file_to_write_path()
        write_to_file(file_to_write_name, fin_text)
    except FileNotFoundError as e:
        print(f"The file on path {path_to_read_file} doesn't exist")
    except FileExistsError as err:
        print(f"The file {file_to_write_name} already exists")
        print(f"User does not want to change the existing file {file_to_write_name}")

if __name__ == "__main__":
    """
    Эта конструкция гарантирует что файл будет исполнен только когда запущен на прямую
    """
    main()
