# Implement a method to perform basic string compression using the counts of repeated characters
# aabcccccaaa => a2b1c5a3
# Return original string if length of compressed string is not smaller than that of original string

def compress(s):
  # SOLUTION I
  # res = ''
  # count = 1
  # res += s[0]

  # for i in range(0, len(s)-1):
  #   if s[i] == s[i+1]:
  #     count += 1
  #   else:
  #     res += str(count)
  #     res += s[i+1]
  #     count = 1
  # res += str(count)

  # if len(res) == (len(s)*2):
  #   print(s)
  # else:
  #   print(res)
  
  
  # SOLUTION II
  #   res = ''
  #   last = s[0]
  #   count = 1
  #   for i in range(1, len(s)):
  #     if s[i] == last:
  #       count += 1
  #     else:
  #       res += last + str(count)
  #       last = s[i]
  #       count = 1
  #   res += last + str(count)

  #   print(res)
  
compress('abccd')
