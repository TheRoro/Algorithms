def sub_array_sum(nums, k):
    hashmap = {0: 1}
    current_sum = 0
    n_sub_arrays = 0

    for n in nums:
        current_sum += n
        diff = current_sum - k
        n_sub_arrays += hashmap.get(diff, 0)
        hashmap[current_sum] = hashmap.get(current_sum, 0) + 1

    return n_sub_arrays


sub_array_sum([1, 1, 1], 2)
