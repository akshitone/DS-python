# count the number of rotations
def count_rotations(nums):

    # length of the list
    nums_length = len(nums)

    # initialize counter
    counter = 0

    # the list is empty or
    # if the first item is less than the last item means that the list is already sorted or
    # length is 1
    if not nums or nums[0] < nums[nums_length - 1] or nums_length == 1:
        return counter

    # start from the second item
    for i in range(1, nums_length):
        counter += 1
        # if the previous item is greater than the current item
        if nums[i-1] > nums[i]:
            return counter


if __name__ == '__main__':
    rotated_list = [5, 6, 9, 0, 2, 3, 4]
    # rotated_list = [1, 2, 3, 4, 5, 6, 7]
    rotated_list = [1]
    result = count_rotations(rotated_list)
    print(result)
