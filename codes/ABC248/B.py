a, b, k = map(int, input().split())
 
ans = 0
 
if a>=b:
  print(ans)
else:
  while a < b:
    a *= k
    ans += 1
  
  print(ans)