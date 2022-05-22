def search_range(nums, target):
    l, r = 0, len(nums) - 1
    ans = [-1, -1]
    
    while l <= r:
        mid = (l + r) // 2
        if target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        else:
            ans[0] = mid
            r = mid - 1

    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        else:
            ans[1] = mid
            l = mid + 1

    return ans
