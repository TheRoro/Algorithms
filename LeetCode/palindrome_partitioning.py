def partition(s):
    # "aab"

    # "a", "a", "b"
    # "aa", b
    # "a", "ab"
    # "aab"

    # "a" "ab"
    # "aa", "b"

    ans = []
    partition = []

    def is_palindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def get_partitions(index=0):
        if index == len(s):
            ans.append(partition.copy())
            return

        # 0 -> 0
        # 0 -> 1
        # 0 -> 2
        for i in range(index, len(s)):
            if is_palindrome(index, i):
                substring = s[index:i + 1]
                partition.append(substring)
                get_partitions(i + 1)
                partition.pop(-1)

    get_partitions()

    return ans
