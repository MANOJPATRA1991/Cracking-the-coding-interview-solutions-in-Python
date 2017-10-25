# Implement a function to reverse a string


def rev(str):
    """
    A function to reverse a string
    Args:
        str(string): The string to reverse
    Returns:
        string: The reversed string
    """
    # SOLUTION I
    return ''.join(reversed(str))

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
