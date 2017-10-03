import itertools

def compress(s):
  res = ''.join('{0}{1}'.format(k, len(list(g))) for k, g in itertools.groupby(s))
  if len(res) < len(s):
    return res
  else:
    return s
    
print(compress('aabcccccaaa'))
