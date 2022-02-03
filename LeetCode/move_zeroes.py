def move_zeroes(nums) -> None:
    zero_pointer = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_pointer] = nums[zero_pointer], nums[i]
            zero_pointer += 1
