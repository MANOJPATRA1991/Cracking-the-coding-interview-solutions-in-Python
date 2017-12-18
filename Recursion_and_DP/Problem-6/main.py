# A method to print all valid combinations of n-pairs of parenthesis.


def parentheses(num):
    """
    Attributes:
        num: Number of pairs
    Returns:
        A generator of all combinations
    """
    if num == 1:
        yield "()"
        return

    for pair in parentheses(num - 1):
        comb1 = "({0})".format(pair)
        comb2 = "(){0}".format(pair)
        comb3 = "{0}()".format(pair)

        yield comb1
        yield comb2
        if comb2 != comb3:
            yield comb3

result = list(parentheses(2))
print(result)