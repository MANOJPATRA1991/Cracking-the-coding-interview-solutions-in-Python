# Find if two strings are permutation of either
# Permutation means having same characters but in different order

def permutation(s,t):
  if (len(s) != len(t)):
    return False
    
  return sorted([c for c in s]) == sorted([c for c in t])

print(permutation("GOD", "OGD"))
