# Given a boolean expression consisting of the symbols 0, 1, &, |, and ^, and
# a desired boolean result value 'result', implement a function to count the
# number of ways of parenthesizing the expression such that it evalues to
# 'result'.

import functools
import collections
import re


def memoize(f):
    """ Minimalistic memoization decorator (*args / **kwargs)
    Based on: http://code.activestate.com/recipes/577219/ """

    cache = {}

    @functools.wraps(f)
    def memf(*args, **kwargs):
        fkwargs = frozenset(kwargs.items())
        if (args, fkwargs) not in cache:
            cache[args, fkwargs] = f(*args, **kwargs)
        return cache[args, fkwargs]
    return memf


def get_operator_indices(exp):
    """
    Get all operator indices
    Args:
        exp(str): Boolean expression
    Returns:
        A generator of the indices where operators
        can be found in the expression
    """
    pattern = "&|\||\^"
    for match in re.finditer(pattern, exp):
        yield match.start()

# Creates a default dictionary of dictionaries
LOGICAL_OPS = collections.defaultdict(dict)
LOGICAL_OPS['&'][True] = [(True, True)]
LOGICAL_OPS['&'][False] = [(False, False), (True, False), (False, True)]
LOGICAL_OPS['|'][True] = [(True, True), (True, False), (False, True)]
LOGICAL_OPS['|'][False] = [(False, False)]
LOGICAL_OPS['^'][True] = [(True,  False), (False, True)]
LOGICAL_OPS['^'][False] = [(True, True), (False, False)]


@memoize
def parenthesize_count(exp, result):
    """
    Calculates the number of ways of parenthesizing the expression so that
    it evaluates to given result
    Args:
        exp(str): A boolean expression
        result(bool): Result of the boolean expression
    Returns:
        Integer: Number of ways of parenthesizing the expression so that
    it evaluates to given result
    """
    if len(exp) == 1:
        value = int(exp)
        return int(bool(value) == result)

    total = 0
    for index in get_operator_indices(exp):
        left = exp[:index]
        op = exp[index]
        right = exp[index+1:]

        for result_left, result_right in LOGICAL_OPS[op][result]:
            total += parenthesize_count(left, result_left) * \
                     parenthesize_count(right, result_right)

    return total

print(parenthesize_count("1^0|0|1", True))
