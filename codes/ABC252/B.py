n,k=map(int,input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
 
a_max=max(a)
hoges=[]
for i,v in enumerate(a):
  if v==a_max: hoges.append(i)
    
for i in hoges:
  if i+1 in b:
    print("Yes")
    exit()
print("No")