
def reverse(s):
    arr = list(s)
    start_index = 0
    end_index = len(arr) -1
    while end_index > start_index:
        arr[end_index], arr[start_index] = arr[start_index], arr[end_index]
        start_index = start_index + 1
        end_index = end_index - 1
    return ''.join(arr)


def is_palindrome(s):
    if s == reverse(s):
        return True
    else:
        return False


if __name__ == "__main__":
    s = "MUKESH"
    print(is_palindrome(s))