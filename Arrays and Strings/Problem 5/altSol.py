# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(N)
def compressBetter(s):
  # check if compression would create a longer string
  size = countCompression(s)
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
      index = setChar(res, last, index, count)
      last = s[i]
      count = 1
  index = setChar(res, last, index, count)
  
  print(''.join(res))
  
  
def setChar(res, last, index, count):
  res[index] = last
  index += 1
  cnt = [c for c in str(count)]
  for c in cnt:
    res[index] = c
    index += 1
  return index
  
def countCompression(s):
  """checks if compressed string is shorter than
  original string"""
  if (s == None or not s):
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
  
compressBetter('aabcccccaaa')
