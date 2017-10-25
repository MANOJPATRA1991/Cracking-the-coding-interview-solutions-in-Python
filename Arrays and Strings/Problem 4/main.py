# write a method to replace all spaces in a string with "%20"
# Given: True length of the string


def replace_spaces(s, len):
    """
    Replaces all spaces in a string with "%20"
    Args:
        s(string): String to work on
        len(int): Length of the string
    """
    # SOLUTION I
    space_count = 0
    num_length = 0
    list_arr = [c for c in s]
    for c in s:
      if c == ' ':
        space_count = space_count + 1
    num_length = len + space_count * 2
    list_arr = list_arr + ['0']*space_count*2
    for i in range (len-1, 0, -1):
      if list_arr[i] == ' ':
        list_arr[num_length-1] = '0'
        list_arr[num_length-2] = '2'
        list_arr[num_length-3] = '%'
        num_length = num_length - 3
      else:
        list_arr[num_length-1] = list_arr[i]
        num_length = num_length-1
    return ''.join(list_arr)

    # SOLUTION II
    # listarr = [c for c in str]
    # for i in range ( 0, len(str), 1):
    #   if listarr[i] ==' ':
    #     listarr.pop(i)
    #     listarr.insert(i, '%20')
    # print(''.join(listarr))

    # SOLUTION III
    # print('%20'.join(s.split(' ')))

    # SOLUTION IV
    # print(s.replace(' ', '%20')
  
  
print(replace_spaces("I am a human", 12))
   
