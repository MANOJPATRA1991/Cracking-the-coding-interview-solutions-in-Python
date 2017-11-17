# Recursive solution

# Implement a method to count number of possible ways to run up a stair with n steps

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
        return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)