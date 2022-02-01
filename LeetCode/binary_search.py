# Iterative
def search(nums, target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1


# Recursive
def binary_search(nums, target, l, r):
    mid = l + (r - l) // 2

    if l > r:
        return -1

    if nums[mid] == target:
        return mid

    if nums[mid] > target:
        return binary_search(nums, target, l, mid - 1)

    if nums[mid] < target:
        return binary_search(nums, target, mid + 1, r)
