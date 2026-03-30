def move_zeroes(nums):
    k = 0  # Pointer for the position of the next non-zero element

    for i in range(len(nums)):
        if nums[i] !=0:
            nums[k], nums[i] = nums[i],  nums[k]
            k+=1
    return nums

nums = [0, 1, 0, 3, 12]
print(move_zeroes(nums))