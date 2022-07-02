
def anagram(first_word, second_word):
    first_list = list(first_word)
    check_anagram = True
    for i in range(len(first_list)):
        if first_list[i] not in second_word:
            check_anagram = False
        break
    return check_anagram


def length_check(first_word, second_word):
    return len(first_word) == len(second_word)


def is_anagram(first_word, second_word):
    if length_check(first_word, second_word):
        return anagram(first_word, second_word)
    else:
        return False


if __name__ == "__main__":
    print(is_anagram('check', 'kcehc'))




