def permute(nums):
    ans = []

    def get_permutations(current_perm=[]):
        if len(current_perm) == len(nums):
            ans.append(current_perm)
            return

        for n in nums:
            permutation_copy = current_perm.copy()
            if n not in permutation_copy:
                permutation_copy.append(n)
                get_permutations(permutation_copy)

    get_permutations()

    return ans
