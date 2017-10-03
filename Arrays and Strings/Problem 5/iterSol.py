import itertools

def compress(s):
  return ''.join('{0}{1}'.format(k, len(list(g))) for k, g in itertools.groupby(s))
  
compress('aabcccccaaa')
