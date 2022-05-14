import itertools
 
n, w = map(int, input().split())
A = list(map(int, input().split()))
 
if n == 1:
  print(1 if A[0] <= w else 0)
elif n == 2:
  filtered = [x for x in A if x <= w]
  print(len(set(filtered)) if sum(A) > w else len(set(filtered)) + 1)
else:
  A.sort()
  filtered = [x for x in A if x <= w]
  one = set(filtered)
  two = itertools.combinations(filtered, 2)
  for x in two:
    hoge = sum(x)
    if hoge <= w:
      one.add(hoge)
      
  three = itertools.combinations(filtered, 3)
  for x in three:
    hoge = sum(x)
    if hoge <= w:
      one.add(hoge)
 
  print(len(one))