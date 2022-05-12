n, a, b = map(int, input().split())
 
for i in range(n):
  ans = "."*b if i%2==0 else "#"*b
  if i%2==0:
    for j in range(2, n+1):
      ans += "."*b if j%2 != 0 else "#"*b
      
  else:
    for j in range(2, n+1):
      ans += "#"*b if j%2 != 0 else "."*b
    
  print((ans + "\n")*a , end="")