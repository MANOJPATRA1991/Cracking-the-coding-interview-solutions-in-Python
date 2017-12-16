# DP solution

# Implement a method to count number of possible ways to run up a stair with n steps taking 1, 2 or 3 steps at a time


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
        res[n] = 0
        for i in range(1, min(n, 3) + 1):
            res[n] += count_ways(n - i, res)
        return res[n]

x = []
print(count_ways(3, x))


