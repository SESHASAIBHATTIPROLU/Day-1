MAX_CHARS = 256
def stringIsomorphic(string1, string2): 
  a = len(string1) 
  b = len(string2) 

  if (a != b): 
    return False
  mark = [False] * MAX_CHARS 
  map = [-1] * MAX_CHARS 

  for i in range(n): 
 
    if map[ord(string1[i])] == -1: 
 
      if mark[ord(string2[i])] == True: 
        return False

      mark[ord(string2[i])] = True
      map[ord(string1[i])] = string2[i] 
    elif map[ord(string1[i])] != string2[i]: 
      return False

  return True

string1 = input("Enter the string 1: ")
string2 = input("Enter the string 2: ")
print(stringIsomorphic(string1, string2))
