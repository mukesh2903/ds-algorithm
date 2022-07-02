

def reverse(arr):
    start_index = 0
    end_index = len(arr) -1
    while end_index > start_index:
        arr[end_index], arr[start_index] = arr[start_index], arr[end_index]
        start_index = start_index + 1
        end_index = end_index - 1
    return arr


if __name__ == '__main__':
    arr = [1, -2, -4, 5, 6]
    print(reverse(arr))



