def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0 or not isinstance(word, str):
        return False
    if low_index >= high_index:
        return True
    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return False
