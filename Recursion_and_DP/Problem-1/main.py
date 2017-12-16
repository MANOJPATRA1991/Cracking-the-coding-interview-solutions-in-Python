# Recursive solution

# Implement a method to count number of possible ways to run up a stair with n steps taking 1, 2 or 3 steps at a time

# Runtime: O(3^n)


def count_ways(n):
    """
    Counts the number of ways to run up a stair with n steps
    Args:
        n(Integer): The number of steps
    Returns:
        Integer: The number of ways to run up the stair
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        total = 0
        for i in range(1, min(n, 3) + 1):
            total += count_ways(n - i)
        return total

print(count_ways(4))
