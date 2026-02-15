def sorted_snail_matrix(input_matrix):
   
    if not input_matrix or not input_matrix[0]:
        return []

    rows, cols = len(input_matrix), len(input_matrix[0])

    
    flat_sorted = sorted(elem for row in input_matrix for elem in row)

    
    result = [[0] * cols for _ in range(rows)]

    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    idx = 0

    while top <= bottom and left <= right:
      
        for i in range(left, right + 1):
            result[top][i] = flat_sorted[idx]
            idx += 1
        top += 1

        
        for i in range(top, bottom + 1):
            result[i][right] = flat_sorted[idx]
            idx += 1
        right -= 1

        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result[bottom][i] = flat_sorted[idx]
                idx += 1
            bottom -= 1

       
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result[i][left] = flat_sorted[idx]
                idx += 1
            left += 1

    return result


if __name__ == "__main__":
    matrix = [
      [25, 7, 1, 19, 12],
        [14, 3, 22, 8, 17],
        [9, 11, 4, 24, 2],
        [18, 16, 6, 10, 21],
        [20, 23, 5, 15, 13]
    ]

    print("Original Matrix:")
    for row in matrix:
        print(row)

    snail_sorted = sorted_snail_matrix(matrix)
    print("\nSorted Snail Matrix:")
    for row in snail_sorted:
        print(row)
