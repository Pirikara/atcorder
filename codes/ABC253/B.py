h,w = map(int, input().split())
s = [input() for _ in range(h)]
 
cood = []
for index, str in enumerate(s):
  fin = str.find("o")
  if fin != -1: cood.append([index, fin])
    
if len(cood) == 2:
  print(abs(cood[0][0]-cood[1][0]) + abs(cood[0][1]-cood[1][1]))
else:
  hoge = cood[0][0]
  result=[]
  for index,i in enumerate(list(s[hoge])):
    if i=="o": result.append(index)
  print(abs(result[0]-result[1]))