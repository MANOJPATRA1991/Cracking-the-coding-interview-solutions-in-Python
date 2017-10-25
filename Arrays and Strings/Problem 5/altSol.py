# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(N)


def compress_better(s):
    """
    Check if compression would create a longer string
    Args:
        s(string): String to check
    Returns:
        String: The compressed string if compressed string has a
                length smaller than length of given string
                else the given string
    """
    size = count_compression(s)
    # Return the string itself if compressed string has
    # a size greater than length of given string
    if size > len(s):
        return s

    # create a list of exactly the same size as that of expected
    # output as we now know the size
    res = [0]*size
    last = s[0]
    index = 0
    count = 1
    for i in range(1, len(s)):
        if s[i] == last:
            count += 1
        else:
            index = set_char(res, last, index, count)
            last = s[i]
            count = 1
    index = set_char(res, last, index, count)

    return ''.join(res)
  
  
def set_char(res, last, index, count):
    """
    Builds the compressed string
    Args:
        res(list): The list to insert the result into
        last(string): The last character compressed
        index(int): The index to start insertion
        count(int): The count appearance of last string
    Returns:
        Integer: The next index to insert in
    """
    res[index] = last
    index += 1
    cnt = [c for c in str(count)]
    for c in cnt:
        res[index] = c
        index += 1
    return index


def count_compression(s):
    """
    checks if compressed string is shorter than
    original string
    Args:
        s(string)
    Returns:
        Integer: 0 or size of the compressed string
    """
    if s is None or not s:
        return 0
    last = s[0]
    count = 1
    size = 0
    for i in range(1, len(s)):
        if s[i] == last:
            count += 1
        else:
            last = s[i]
            size += 1 + len(str(count))
            count = 1
    size += 1 + len(str(count))

    return size
  
compressed = compress_better('aabcccccaaa')
print(compressed)
