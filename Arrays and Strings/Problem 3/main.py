# Find if two strings are permutation of either
# Permutation means having same characters but in different order

def permutation(s,t):
  # SOLUTION I
  # if (len(s) != len(t)):
  #   return False
    
  # return sorted([c for c in s]) == sorted([c for c in t])
  
  # SOLUTION II
  if (len(s) != len(t)):
    return False
    
  letters = [0]*256
  for c in [i for i in s]:
    letters[ord(c)] = letters[ord(c)] + 1
  
  for c in [j for j in t]:
    if (letters[ord(c)]-1 < 0):
      return False
  
  return True

print(permutation("GOD", "GOD"))
