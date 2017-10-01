# Implement a function to reverse a string

def rev(str):
  # SOLUTION I
  # return ''.join(reversed(str))
  
  # SOLUTION II
  # return str[::-1]
  
  # SOLUTION III
  begin, end = 0, len(str)-1
  revStr = [c for c in str]
  while (begin < end):
    revStr[end], revStr[begin] = revStr[begin], revStr[end]
    begin = begin + 1
    end = end - 1
  return ''.join(revStr)
  
print(rev("flash"))
