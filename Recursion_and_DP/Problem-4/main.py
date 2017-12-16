# Write a method to return all subsets of a set


def subsets(seq):
    """
    Return a generator of all the subsets.
    Args:
        seq: Given set
    """
    set_ = list(seq)

    if len(set_) < 1:
        yield set_
        return

    last = [set_.pop()]

    for subset in subsets(set_):
        yield subset
        yield subset + last


def find_subsets(l):
    """
    Main caller function
    Args:
        l: Given set
    """
    result = list(subsets(l))   # [[], ['b'], ['a'], ['a', 'b']]
    result.sort()               # [[], ['a'], ['a', 'b'], ['b']]
    result.sort(key=len)        # [[], ['a'], ['b'], ['a', 'b']]
    return result

print(find_subsets(('a', 'b')))
