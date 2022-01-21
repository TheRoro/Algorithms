def remove_element(nums, val):
    k = 0
    for x in nums:
        if x != val:
            k += 1

    last_pointer = len(nums) - 1

    for i in range(k):
        if nums[i] == val:
            while nums[last_pointer] == val:
                last_pointer -= 1
            nums[i], nums[last_pointer] = nums[last_pointer], nums[i]
            last_pointer -= 1

    print(nums)


remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2)
