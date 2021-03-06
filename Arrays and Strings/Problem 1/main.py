# Algorithm to check if a string has all unique characters


def is_unique_string(str):
    # Solution I
    #
    # TIME COMPLEXITY = O(n), n = length of the string
    # SPACE COMPLEXITY = O(1)
    #
    # # if length of string is greater than 128,
    # # it definitely contains duplicate characters
    if len(str) > 128:
        return False
    u_chars = set()
    for c in str:
        # if character already present in uchars
        # then we have a duplicate character
        if c in u_chars:
            return False
        u_chars.add(c)
    # unique characters in string
    return True

    # Solution II
    # return len(set(str)) == len(str)

    # Solution III
    #
    # TIME COMPLEXITY = O(n), n = length of the string
    # SPACE COMPLEXITY = O(1/8)
    #
    # checker = 0
    # for c in str:
    #   val = ord(c) - ord('a')
    #   try:
    #     # if character position already 1 in checker,
    #     # value of if conditional will be true
    #     if ((checker & (1 << val)) > 0):
    #       return False
    #     # update particular bit in checker as per position of c
    #     checker = checker | (1 << val)
    #   except ValueError as v:
    #     continue
    # return True
  
print(is_unique_string("abc de"))
print(is_unique_string("12edfc"))
