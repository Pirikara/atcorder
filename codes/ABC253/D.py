#最大公約数
def gcd(x,y):
  if x==0:
    return y
  return gcd(y%x,x)

#最小公倍数
def lcm(x,y):
  return (x*y)//gcd(x,y)

# gの倍数がn個あるとして、その総和
# n*(1+n)//2 が 1 ~ n の総和。これに g を掛けると g の倍数の総和が求まる。 
def sumSequence(g,n):
  return g*(1+n)*n//2
 
n,a,b  = map(int,input().split())

# 欲しいのは、1 ~ n の総和から a , b の倍数の総和を取り除き、a , b の最小公倍数の倍数の総和を足した結果
ans = sumSequence(1,n) - sumSequence(a,n//a) - sumSequence(b,n//b) + sumSequence(lcm(a,b),n//lcm(a,b))
 
print(ans)