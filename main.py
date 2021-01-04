# Given two strings, write a method to decide if one is a permutation of the other. 
def checkPermutation(string1, string2):
  #sort them

  #print("testing1")
  string1sorted = sorted(string1)
  string2sorted = sorted(string2)

  #print("test")


  #need to account spaces

  length1 = len(string1)
  length2 = len(string2)
  if(length1 != length2):
    #print("no")
    return False
  
  if(string1sorted == string2sorted):
    #print("no")
    return True



input1= "banana"
input2= "bna aan"

if(checkPermutation(input1, input2)):
  print("yes")
else:
  print("no")