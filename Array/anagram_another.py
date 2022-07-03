
def is_anagram(str1, str2):
    # check length of both the string and if it doesn't match then return false
    if len(str1) != len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


if __name__ == "__main__":
    print(is_anagram("restfuls", "fluster"))

