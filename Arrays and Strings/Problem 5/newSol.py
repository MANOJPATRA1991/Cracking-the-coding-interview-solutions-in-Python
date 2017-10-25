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
    if size > len(s):
        return s
    
    res = []
    last = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == last:
            count += 1
        else:
            res.append(last)
            res.append(str(count))
            last = s[i]
            count = 1
    res.append(last)
    res.append(str(count))

    return ''.join(res)
  
  
def count_compression(s):
    """
    Checks if compressed string is shorter than
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
