
def anagram(first_word, second_word):
    word_found = True
    first_list = list(first_word)
    i = 0
    while i <= len(first_list) - 1:
        if first_list[i] in second_word:
            word_found = True
        else:
            word_found = False
            break
        i = i + 1
    check_length = len(first_word) == len(second_word)
    result = word_found == check_length
    return result


if __name__ == "__main__":
    print(anagram('check', 'kcehc'))




