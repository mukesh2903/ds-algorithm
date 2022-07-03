
def dutch_flag_problem(nums, pivot=1):
    i = 0
    j = 0
    k = len(nums) - 1
    while j <= k:
        # current value is 0
        if num[j] < pivot:
            swap(nums, i, j)
            i = i+1
            j = j+1
        # current value is 2
        elif nums[j] > pivot:
            swap(nums, j, k)
            k = k - 1
            j = j + 1
        # current element is 1
        else:
            j = j + 1
    return nums


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":
    num = [0, 1, 0, 2, 2, 1, 1]
    print(dutch_flag_problem(num))





