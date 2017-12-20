# Given an infinite number of quarters (25 cents), dimes (10 cents),
# nickels (5 cents) and pennies (1 cent), write code to calculate the
# number of ways of representing n cents.

import functools


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


@memoize
def make_change(amount, coin=None):
    """
    Find number of ways of making change for a given amount
    Args:
        amount(int): The amount for which we need to find the number of ways
        coin(int): Default coin with which to make
    Returns:
        Integer: Number of ways of making change for the given amount
    """
    if not amount:
        return 1

    coins = [1, 5, 10, 25]

    if not coin:
        # Maximum valued coin we can use for the given amount
        coin = max(c for c in coins if c <= amount)

    if coin == 1:
        return 1

    # Next maximum valued coin
    next_coin = coins[coins.index(coin) - 1]

    total = 0
    # Maximum number of coin-values required to
    # make change if one of the coins is "coin"
    max_coins = amount // coin

    for n in range(max_coins + 1):
        remainder = amount - (n * coin)
        total += make_change(remainder, next_coin)
    return total

print("The number of ways of making change for "
      "{0} = {1}".format(10, make_change(10)))

# Output
# The number of ways of making change for 10 = 4
