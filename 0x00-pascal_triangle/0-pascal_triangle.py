def pascal_triangle(num_rows):
    if num_rows < 1:
        return []
    if num_rows == 1:
        return [[1]]

    triangle = [[1]]

    for i in range(1, num_rows):
        prev_row = triangle[i - 1]
        cur_row = []

        cur_row.append(1)

        for j in range(1, len(prev_row)):
            cur_row.append(prev_row[j] + prev_row[j - 1])

        cur_row.append(1)

        triangle.append(cur_row)

        return triangle
