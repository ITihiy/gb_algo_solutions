# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
import hashlib


def get_all_substrings(input_str):
    return [input_str[i:j] for i in range(len(input_str)) for j in range(i + 1, len(input_str) + 1)]


def get_number_of_hashes(list_of_substrings):
    return len(set(hashlib.sha1(str_.encode('utf-8')).hexdigest() for str_ in list_of_substrings))


if __name__ == '__main__':
    s = input('Please enter a string: ')
    substrings = get_all_substrings(s)
    print(substrings)
    print(get_number_of_hashes(substrings))
