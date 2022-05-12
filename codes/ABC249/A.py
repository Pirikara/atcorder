
# パターン1
def solve(a, b, c, x):
  # a+c周期を終える回数
  q = x // (a + c)
  # a+c周期を終えて残る秒数
  r = x % (a + c);
  # a以上秒数が残っていても進むことはないため、最小値をとる
  return (q * a + min(a, r)) * b;

a, b, c, d, e, f, x = map(int, input().split())

ta = solve(a, b, c, x)
ao = solve(d, e, f, x)
print("Takahashi" if ta > ao else "Aoki" if ta < ao else "Draw")


# パターン2
a, b, c, d, e, f, x = map(int, input().split())
 
ta = 0
ao = 0
 
# taはa + c秒の間にb動く
# aoはd + f秒の間にe動く
for i in range(x):
  ta += b if i%(a+c) < a else 0
  ao += e if i%(d+f) < d else 0
  
print("Takahashi" if ta > ao else "Aoki" if ta < ao else "Draw")