# 方針: 0~9について、それぞれの数字で揃うまでにかかる秒数の最小値を総当たりで検証する

n=int(input())
s=[input() for _ in range(n)]
# c[i][j]: 数字iがsのj番目に出てくる回数
c=[[0]*10 for _ in range(10)]
for i in range(n):
  for j in range(10):
    c[int(s[i][j])][j]+=1
 
# 揃うのにかかる時間を返す
def solve(x):
  rem=n
  for t in range(10**10):
    if c[x][t%10] > 0:
      c[x][t%10]-=1
      rem-=1
    if rem == 0: return t
    
print(min(solve(i) for i in range(10)))