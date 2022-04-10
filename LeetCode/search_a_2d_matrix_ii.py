def search_matrix(matrix, target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])

    r, c = rows - 1, 0

    # Overall Complexity O(n*log(m))

    while r >= 0 and c < cols:
        print(matrix[r][c])
        if target == matrix[r][c]:
            return True
        elif target < matrix[r][c]:
            r -= 1
        else:
            c += 1

    return False
