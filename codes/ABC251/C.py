N = int(input())

origin = {}
val, idx = 0, 0
for i in range(N):
  data = input().split()
  s, t = data[0], int(data[1])
  if s not in origin:
    origin[s] = t
    if t > val:
      val = t
      idx = i
print(idx+1)