# Write a method to sort an array of strings so that all the anagrams are next to each other.


def sort(_str):
    """
    Sorts the list such that all the anagrams are next to each other
    Args:
        _str: List of strings
    """
    _hash = dict()

    # Store sorted string as key and list of anagrams
    # as value in the dictionary _hash
    for s in _str:
        key = ''.join(sorted(s))
        if key not in _hash.keys():
            _hash[key] = []
        _hash[key].append(s)

    index = 0

    # Update the string list with all the sorted lists
    # of anagrams for each key in the dictionary _hash
    for key in _hash.keys():
        for t in _hash[key]:
            _str[index] = t
            index += 1

    return _str

result = sort(['acre', 'earth', 'race', 'heart', 'care'])
print(result)
