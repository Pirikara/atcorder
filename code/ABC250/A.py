# 入力を受け取る
h, w = map(int, input().split())
r, c = map(int, input().split())
 
# 辺で隣接するマスの最大値は4
# マス(r, c)の位置について、r == 1, c == 1, r == h, c == wのそれぞれの条件下で隣接するマスが1つ減る
print(4 - sum([r == 1, c == 1, r == h, c == w]))