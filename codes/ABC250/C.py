n,q=map(int,input().split())
ans, index = list(range(n)), list(range(n))

for _ in range(q):
  x=int(input())
  x-=1
  pos=index[x]
  if pos!=n-1:
    x2=ans[pos+1]
    ans[pos]=x2
    ans[pos+1]=x
    index[x]=pos+1
    index[x2]=pos
  else:
    x2=ans[pos-1]
    ans[pos]=x2
    ans[pos-1]=x
    index[x]=pos-1
    index[x2]=pos
for i in range(n):
  ans[i]+=1
print(*ans)