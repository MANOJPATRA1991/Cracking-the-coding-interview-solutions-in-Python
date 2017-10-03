# write a method to replace all spaces in a string with "%20"
# Given: True length of the string

def replaceSpaces(str, length):

  # SOLUTION I
  # spaceCount = 0
  # numLength = 0
  # listArr = [c for c in str]
  # for c in str:
  #   if c == ' ':
  #     spaceCount = spaceCount + 1
  # numLength = length + spaceCount*2
  # listArr = listArr + ['0']*spaceCount*2
  # for i in range (length-1, 0, -1):
  #   if listArr[i] == ' ':
  #     listArr[numLength-1] = '0'
  #     listArr[numLength-2] = '2'
  #     listArr[numLength-3] = '%'
  #     numLength = numLength - 3
  #   else:
  #     listArr[numLength-1] = listArr[i]
  #     numLength = numLength-1
  # return ''.join(listArr)
      
  #SOLUTION II
  # listarr = [c for c in str]
  # for i in range ( 0, len(str), 1):
  #   if listarr[i] ==' ':
  #     listarr.pop(i)
  #     listarr.insert(i, '%20')
  # print(''.join(listarr))
      
replacespaces("i am a human", 12)      
  
  
print(replaceSpaces("I am a human", 12))  
   
