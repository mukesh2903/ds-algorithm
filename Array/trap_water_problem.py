def max_left(nums):
    arr = [0 for i in range(len(nums))]
    for i in range(len(nums) - 1):
        if arr[i] < nums[i]:
            arr[i+1] = nums[i]
        else:
            arr[i+1] = arr[i]
    return arr


def max_right(nums):
    arr = [0 for i in range(len(nums))]
    for i in range(len(nums)-2, -1, -1):
        if arr[i+1] < nums[i+1]:
            arr[i] = nums[i+1]
        else:
            arr[i] = arr[i+1]
    return arr


def calc_min(nums):
    left_arr = max_left(nums)
    right_arr = max_right(nums)
    for i in range(len(left_arr)):
        if left_arr[i] > right_arr[i]:
            left_arr[i] = right_arr[i]
        if left_arr[i] - nums[i] < 0:
            nums[i] = 0
        else:
            nums[i] = left_arr[i] - nums[i]
    return nums


if __name__ == "__main__":
    print(sum(calc_min([2,1,0,3,4,2])))





