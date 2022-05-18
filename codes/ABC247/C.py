# 再帰処理
n = int(input())
 
def S(n):
  if n == 1:
    return [1]
  else:
    return S(n-1) + [n] + S(n-1)
 
print(*S(n))

# メモ化再帰
n = int(input())

memo = {}
def S(n):
  if n in memo:
    return memo[n]
  if n == 1:
    num = [1]
  else:
    num = S(n-1) + [n] + S(n-1)
  memo[n] = num
  return num

print(*S(n))

# 動的計画法
n = int(input())
dp = [[] for _ in range(n+1)]

dp[1] = 1
for n in range(2, n+1):
  dp[n] = dp[n-1] + [n] + dp[n-1]

print(*dp[n])