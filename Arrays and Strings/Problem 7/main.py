# Write an algorithm such that if an element in an MXN matrix is  0
# its entire row and column are set to 0


def set_zeros(matrix):
    row = [0]*len(matrix)
    column = [0]*len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True

    for i in range(len(row)):
        if row[i]:
            nullify_row(matrix, i)

        for j in range(len(column)):
            if column[j]:
                nullify_column(matrix, j)


def nullify_row(matrix, row):
  for j in range(len(matrix[0])):
    matrix[row][j] = 0


def nullify_column(matrix, column):
  for i in range(len(matrix)):
    matrix[i][column] = 0
    
x = [
      [1, 2, 3],
      [4, 5, 0],
      [7, 8, 9],
      [0, 11, 12]
    ]

for i in x:
    print(i)
  
set_zeros(x)

print("\n\n")

for i in x:
    print(i)

# OUTPUT

# [0, 2, 0]
# [0, 0, 0]
# [0, 8, 0]
# [0, 0, 0]
