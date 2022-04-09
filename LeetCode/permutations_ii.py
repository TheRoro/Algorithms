from collections import Counter


def permute_unique(nums):
    ans = []
    perms = []
    count = Counter(nums)

    def get_permutations():
        if len(perms) == len(nums):
            ans.append(perms.copy())
            return

        for n in count:
            if count[n] > 0:
                perms.append(n)
                count[n] -= 1
                get_permutations()

                count[n] += 1
                perms.pop(-1)

    get_permutations()

    return ans
