def minimum_swaps(arr):
    positions = {}
    swaps = 0

    for i in range(len(arr)):
        if arr[i] not in positions:
            positions[arr[i]] = i

    for i in range(len(arr)):
        actual_num = i + 1
        if positions[actual_num] != i:
            new_pos = i
            swap_value = arr[new_pos]
            arr[new_pos] = actual_num
            arr[positions[actual_num]] = swap_value
            positions[swap_value] = positions[actual_num]
            positions[actual_num] = new_pos
            swaps += 1

    return swaps


print(minimum_swaps([1, 3, 5, 2, 4, 6, 7]))
