def getLongestAdjacentSequence(matrix):
    matrix_rows = len(matrix)
    matrix_cols = len(matrix[0])

    visited = [[False] * matrix_rows for i in range(matrix_cols)]
    stack = []
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    maxSeqLenght = 0

    for row in range(matrix_rows):
        for col in range(matrix_cols):
            if visited[row][col]:
                continue
            sequenceLenght = 0
            stack.append([row, col])
            while stack:
                currentCell = stack.pop()
                currentRow = currentCell[0]
                currentCol = currentCell[1]

                if (visited[currentRow][currentCol]):
                    continue
                current = matrix[currentRow][currentCol]
                visited[currentRow][currentCol] = True
                sequenceLenght += 1

                for direction in directions:
                    adjacentRow = currentRow + direction[0];
                    adjacentCol = currentCol + direction[1];

                    if adjacentCol < 0 or adjacentCol >= matrix_cols or adjacentRow < 0 or adjacentRow >= matrix_rows or \
                            visited[adjacentRow][adjacentCol]:
                        continue

                    adjacent = matrix[adjacentRow][adjacentCol]
                    if current == adjacent:
                        stack.append([adjacentRow, adjacentCol])

            maxSeqLenght = max(sequenceLenght, maxSeqLenght)
        return maxSeqLenght


test1 = [
    [
        'R', 'R', 'B',
    ],
    [
        'G', 'G', 'R',
    ],
    [
        'R', 'B', 'G',
    ]]

test2 = [
    [
        'R', 'R', 'R', 'G',
    ],
    [
        'G', 'B', 'R', 'G',
    ],
    [
        'R', 'G', 'G', 'G',

    ],
    [
        'G', 'G', 'B', 'B'
    ]]

test3 = [
    [
        'R', 'R', 'B', 'B', 'B', 'B',
    ],
    [
        'R', 'R', 'B', 'B', 'G', 'B',
    ],
    [
        'B', 'R', 'B', 'B', 'G', 'B',
    ],
    [
        'B', 'B', 'R', 'B', 'G', 'B',
    ],
    [
        'R', 'B', 'R', 'B', 'R', 'B',
    ],
    [
        'R', 'B', 'B', 'B', 'G', 'B',
    ]]
matrix_rows = 1000
matrix_cols = 1000
test4 = [[0] * matrix_cols] * matrix_rows

for row in range(matrix_rows):
    for col in range(matrix_cols):
        test4[row][col] = 'R'

print(getLongestAdjacentSequence(test1))
print(getLongestAdjacentSequence(test2))
print(getLongestAdjacentSequence(test3))
print(getLongestAdjacentSequence(test4))
