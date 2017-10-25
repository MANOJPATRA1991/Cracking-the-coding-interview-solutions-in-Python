# Given an image represented by an NXN matrix, where each pixel in
# the image is 4 bytes, write a method to rotate the image by 90
# degrees.


# TIME COMPLEXITY = O(N^2),
# as we need to touch N^2 elements


def rotate(matrix, n):
    """
    Rotate the matrix by 90 degrees
    Args:
        matrix(list): list of lists (2 X 2)
        n(int): size of the matrix
    Returns:
        List: Rotated matrix
    """
    # for a nxn matrix, there will be n/2 layers
    y = n // 2
    for layer in range(0,y):
        first = layer
        last = n - 1 - layer
        for i in range(first,last):
            offset = i - first
            top = matrix[first][i]

            matrix[first][i] = matrix[last-offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = top
    return matrix
  
x = [ ['p00', 'p01', 'p02', 'p03'],
      ['p10', 'p11', 'p12', 'p13'],
      ['p20', 'p21', 'p22', 'p23'],
      ['p30', 'p31', 'p32', 'p33'] ]

for i in rotate(x,4):
    print(i)