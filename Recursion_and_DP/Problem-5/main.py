# A method to compute all permutations of a string of unique characters.
# O(n!)since there are n! permutations


def permutations(s):
    """
    Attributes:
        s(String): String of unique characters
    Returns:
        A generator of all permutations
    """
    if len(s) == 1:
        yield s

    for index, letter in enumerate(s):
        remainder = s[:index] + s[index+1:]
        for word in permutations(remainder):
            yield letter + word

result = list(permutations('abc'))
print(result)