# Check if string s2 is a rotation of string s1 assuming we have only one function to detect if a string is a substring of another string

def isRotation(s1, s2):
  if (len(s1) == len(s2) and (len(s1) > 0)):
    s1 += s1
    return s1.find(s2) > -1
  return False
  
print(isRotation('waterbottle', 'erbottlewat'))
    
