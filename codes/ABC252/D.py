from collections import Counter
import math
 
n=int(input())
a=list(map(int,input().split()))
c=Counter(a)
ans=math.comb(n,3)
 
for v in c.values():
  ans-=math.comb(v,2)*(n-v)
  ans-=math.comb(v,3)
 
print(ans)