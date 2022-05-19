n, k, x = map(int, input().split())
a = list(map(int, input().split()))

# 以下を実行すると、aはクーポンを充てた結果0円にならない最小の価格
# kは余ったクーポンの数を表す
for i in range(n):
  print(k, a[i], x, a[i]//x)
  c = min(k, a[i]//x)
  a[i], k = a[i]-c*x,k-c

# 余ったクーポンk枚分は0円とすることができるので、
# ソートした上で価格の大きいものをk枚分除いたものを合計すれば最小値が得られる
print(sum(sorted(a)[:n-k]))