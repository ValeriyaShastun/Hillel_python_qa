import time

def decorator(func):
    dict_to_check_num = {}
    def wrapper(number):
        if number in dict_to_check_num:
            return dict_to_check_num[number]
        else:
            dict_to_check_num.update({number: func(number)})
            return dict_to_check_num[number]
    return wrapper


@decorator
def main(i):
    time.sleep(i / 10)
    return i ** 2

if __name__ == "__main__":
    start = time.time()
    results = []
    values = (1, 2, 3, 2, 3, 1, 2, 2, 3, 4, 1, 2, 3, 2, 1, 4, 4, 1, 2, 4)
    print(values)
    for i in values:
        results.append(main(i))
    print(results)
    end = time.time()
    print(f"Total time: {end - start}")

# without @decorator
# (1, 2, 3, 2, 3, 1, 2, 2, 3, 4, 1, 2, 3, 2, 1, 4, 4, 1, 2, 4)
# [1, 4, 9, 4, 9, 1, 4, 4, 9, 16, 1, 4, 9, 4, 1, 16, 16, 1, 4, 16]
# Total time: 4.7612340450286865

# with @decorator
# (1, 2, 3, 2, 3, 1, 2, 2, 3, 4, 1, 2, 3, 2, 1, 4, 4, 1, 2, 4)
# [1, 4, 9, 4, 9, 1, 4, 4, 9, 16, 1, 4, 9, 4, 1, 16, 16, 1, 4, 16]
# Total time: 1.0076038837432861