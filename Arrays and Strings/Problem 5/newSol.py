def compressBetter(s):
  # check if compression would create a longer string
  size = countCompression(s)
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
  
  print(''.join(res))
  
  
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
