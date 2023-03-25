def is_anagram(first_string: str, second_string: str):
    first_string_list = [letter.lower() for letter in first_string]
    second_string_list = [letter.lower() for letter in second_string]
    merge_sort(first_string_list, 0, len(first_string_list) - 1)
    merge_sort(second_string_list, 0, len(second_string_list) - 1)
    string1 = join_chars(first_string_list)
    string2 = join_chars(second_string_list)
    return (string1, string2, compare_strings(string1, string2))


def compare_strings(str1: str, str2: str) -> bool:
    if str1 == "" or str2 == "":
        return False
    return str1 == str2


def merge_sort(data: list, start: int, end: int):
    if start < end:
        middle = (start + end) // 2
        merge_sort(data, start, middle)
        merge_sort(data, middle + 1, end)
        merge(data, start, middle, end)


def merge(data: list, start: int, middle: int, end: int):
    temp_list = []
    left_list_index = start
    right_list_index = middle + 1

    while left_list_index <= middle and right_list_index <= end:
        if data[left_list_index] <= data[right_list_index]:
            temp_list.append(data[left_list_index])
            left_list_index += 1
        else:
            temp_list.append(data[right_list_index])
            right_list_index += 1

    while left_list_index <= middle:
        temp_list.append(data[left_list_index])
        left_list_index += 1

    while right_list_index <= end:
        temp_list.append(data[right_list_index])
        right_list_index += 1

    update_list(data, temp_list, start, end)


def update_list(data: list, sub_data: list, start: int, end: int):
    index = start

    while index <= end:
        data[index] = sub_data[index - start]
        index += 1


def join_chars(data: list):
    string = ""
    for char in data:
        string += char
    return string
