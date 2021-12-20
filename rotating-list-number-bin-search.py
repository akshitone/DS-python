# count the number of rotations
def count_rotations(nums):

    # low and high index
    low, high = 0, len(nums) - 1

    # the list is empty or
    # if the first item is less than the last item means that the list is already sorted or
    # length is 1
    # then return 0
    if not nums or nums[0] < nums[high - 1] or high == 1:
        return low

    # while low index is less than or equal to high index
    while low <= high:

        # mid index
        mid = (low + high) // 2
        # mid number
        mid_number = nums[mid]

        # if mid index is greater than 0 and mid number is less than previous number
        if mid > 0 and mid_number < nums[mid-1]:
            # return mid index
            return mid
        # if mid index number is greater than the last number
        elif mid_number > nums[high]:
            # move low index to mid index + 1
            low = mid + 1
        else:
            # move high index to mid index - 1
            high = mid - 1

    # return 0 if the list is empty
    return 0


if __name__ == '__main__':
    rotated_list = [7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6]
    # rotated_list = [1, 2, 3, 4, 5, 6, 7]
    # rotated_list = [1]
    rotated_list = [5, 6, 6, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]
    result = count_rotations(rotated_list)
    print(result)
