def sort_colors_bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]

    return nums


def sort_colors(nums):
    dicty = {}
    for n in nums:
        if n in dicty:
            dicty[n] += 1
        else:
            dicty[n] = 1

    counter = 0
    maxi = 0

    for el in dicty:
        maxi = max(maxi, el)

    for i in range(maxi+1):
        if i in dicty:
            for n in range(dicty[i]):
                nums[counter] = i
                counter += 1

    return nums


def sort_colors2(nums):
    memo = [0, 0, 0]
    for n in nums:
        memo[n] += 1

    counter = 0

    for i in range(memo[0]):
        nums[counter] = 0
        counter += 1

    for i in range(memo[1]):
        nums[counter] = 1
        counter += 1

    for i in range(memo[2]):
        nums[counter] = 2
        counter += 1

    return nums


print(sort_colors2([2, 0, 2, 1, 1, 0]))
