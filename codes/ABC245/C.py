n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
# dp[i]は、Xiまでを考えた時にA[i] or B[i]がXiになりうるか
dp_a = [False]*(n) 
dp_b = [False]*(n)
 
dp_a[0] = dp_b[0] = True
 
for i in range(1, n):
  if dp_a[i-1]:
    if abs(a[i]-a[i-1]) <= k: dp_a[i] = True
    if abs(b[i] - a[i-1]) <= k: dp_b[i] = True
  if dp_b[i-1]:
    if abs(b[i] - b[i-1]) <= k: dp_b[i] = True
    if abs(a[i] - b[i-1]) <= k: dp_a[i] = True
 
print("Yes" if dp_a[n-1] or dp_b[n-1] else "No")