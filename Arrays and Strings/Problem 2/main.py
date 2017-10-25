# Implement a function to reverse a string


def rev(s):
    """
    A function to reverse a string
    Args:
        s(string): The string to reverse
    Returns:
        string: The reversed string
    """
    # SOLUTION I
    return ''.join(reversed(s))

    # SOLUTION II
    # return str[::-1]

    # SOLUTION III
    #   begin, end = 0, len(str)-1
    #   revStr = [c for c in str]
    #   while (begin < end):
    #     revStr[end], revStr[begin] = revStr[begin], revStr[end]
    #     begin = begin + 1
    #     end = end - 1
    #   return ''.join(revStr)

    # SOLUTION IV
    #   if str1 != "":
    #         return str1[-1:] + rev(str1[:-1])
    #     else:
    #         return ""
    #
  
print(rev("flash"))