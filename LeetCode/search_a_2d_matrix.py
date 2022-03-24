def search_matrix(matrix, target) -> bool:
    rows, cols = len(matrix), len(matrix[0])

    top, bottom = 0, rows - 1

    while top <= bottom:
        mid_row = (top + bottom) // 2
        if target > matrix[mid_row][-1]:
            top = mid_row + 1
        elif target < matrix[mid_row][0]:
            bottom = mid_row - 1
        else:
            break

    if not (top <= bottom):
        return False

    row = (top + bottom) // 2
    left, right = 0, cols - 1

    while left <= right:
        m = (left + right) // 2
        if target == matrix[row][m]:
            return True
        elif target < matrix[row][m]:
            right = m - 1
        else:
            left = m + 1

    return False
