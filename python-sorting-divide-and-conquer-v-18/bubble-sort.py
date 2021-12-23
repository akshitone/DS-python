def bubble_sort(nums):  # O(n^2)
    # make a copy of the list
    nums = list(nums)

    # for each element in the list
    for i in range(len(nums)):
        # for each element after the current element
        for j in range(len(nums) - i - 1):
            # if the current element is greater than the next element
            if nums[j] > nums[j + 1]:
                # swap the elements
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    
    # return the sorted list
    return nums


lst = [5, 6, 4, 7, 3, 8, 2, 9, 1]
result = bubble_sort(lst)

print("Original list: ", lst)
print("Sorted list: ", result)
