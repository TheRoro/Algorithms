def generate_parenthesis(n):
    ans = []
    stack = []

    def get_parenthesis(open_count=0, close_count=0):
        if open_count == n == close_count:
            string = "".join(stack)
            ans.append(string)
            return

        if open_count < n:
            stack.append("(")
            get_parenthesis(open_count + 1, close_count)
            stack.pop(-1)

        if close_count < open_count:
            stack.append(")")
            get_parenthesis(open_count, close_count + 1)
            stack.pop(-1)

    get_parenthesis()

    return ans
