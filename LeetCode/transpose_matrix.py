def transpose(mat):

    cols = len(mat[0])
    rows = len(mat)

    ans = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(cols):
        for j in range(rows):
            ans[i][j] = mat[j][i]

    return ans


print(transpose([[1,2,3],[4,5,6]]))
