def locate_num(nums, query):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_number = nums[mid]
        print("low:", low, "high:", high, "mid:",
              mid, "mid_number:", mid_number)
        if mid_number == query:
            return mid + 1
        # elif (mid_number < query or mid_number > nums[high]) and query <= nums[high]:
        elif mid_number >= nums[low]:
            if query > mid_number or query < nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if query < mid_number or query > nums[high]:
                high = mid - 1
            else:
                low = mid + 1

    return -1


if __name__ == '__main__':
    rotated_list = [9, 10, 11, 12, 0, 2, 3, 4, 5, 6, 7, 8]
    result = locate_num(rotated_list, 8)
    print(result)
