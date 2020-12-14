arr = [1, 3, 5, 7, 9, 11, 13]

def binary_search(a, val, l=0, r = len(arr) - 1):
    mid = l + (r - l) // 2
    if r >= l:
        if a[mid] == val:
            return mid
        elif a[mid] > val:
            return binary_search(a, val, l, mid - 1)
        else:
            return binary_search(a, val, mid + 1, r)
    else:
        return False

print(binary_search(arr, 13))