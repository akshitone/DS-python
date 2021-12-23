def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums


lst = [5, 6, 4, 7, 3, 8, 2, 9, 1]
result = insertion_sort(lst)

print("Original list: ", lst)
print("Sorted list: ", result)


def insertion_sort_v2(nums):
    # for each element in the list
    for i in range(1, len(nums)):
        # get the current element
        cur = nums[i]
        # set the index of the previous element
        j = i-1

        # while the previous element is greater than the current element
        while j >= 0 and nums[j] > cur:
            # move the previous element to the next index
            nums[j+1] = nums[j]
            # decrement the index
            j -= 1

        # insert the current element into the next index
        nums[j+1] = cur

    # return the sorted list
    return nums
