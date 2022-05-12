s = input().strip()

def includeUpperCase(str):
  return not(str.lower() == str)
  
def includeLowerCase(str):
  return not(str.upper() == str)
  
def isNotDuplicate(str):
  return len(list(set(str))) == len(str)

def isPerfect(str):
  return (includeUpperCase(str) and includeLowerCase(str) and isNotDuplicate(str))

print("Yes" if isPerfect(s) else "No")