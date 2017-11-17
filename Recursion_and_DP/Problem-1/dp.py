# DP solution

# Implement a method to count number of possible ways to run up a stair with n steps taking 1, 2 or 3 steps at a time
import array


def count_ways(n, res):
    """
    Counts the number of ways to run up a stair with n steps
    Args:
        n(Integer): The number of steps
        res(List): To store sub-problem values
    Returns:
        Integer: The number of ways to run up the stair
    """
    res = [-1]*(n+1)
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif res[n] > -1:
        return res[n]
    else:
        res[n] = count_ways(n - 1, res) + count_ways(n - 2, res) + count_ways(n - 3, res)
        return res[n]

x = []
print(count_ways(3, x))


