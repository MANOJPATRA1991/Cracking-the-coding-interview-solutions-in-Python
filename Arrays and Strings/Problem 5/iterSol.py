import itertools


def compress(s):
    """
    Compress a string
    Args:
        s(string): String to compress
    Returns:
        String: The compressed string
    """
    res = ''.join('{0}{1}'.format(k, len(list(g))) for k, g in itertools.groupby(s))
    if len(res) < len(s):
        return res
    else:
        return s

compressed =compress('aabcccccaaa')
print(compressed)