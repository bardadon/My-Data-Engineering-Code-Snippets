def nth_highest_number(nums, n):
    n = n - 1
    
    # Insertion Sort
    for i in range(1, len(nums)):

        temp = nums[i]
        j = i - 1

        while j>=0 and temp > nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = temp

    return nums[n]

