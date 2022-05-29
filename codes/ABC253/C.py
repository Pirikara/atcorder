# dictを使って、それぞれの数字の個数を管理する
from collections import defaultdict
q = int(input())
s = defaultdict(int)
# maxとminの値を管理する
min_v = 10**9+1
max_v = 0
for i in range(q):
    que = list(map(str,input().split()))
    if que[0] == "1":
        # que 1の時、 keyが x の value を 1 追加する
        s[int(que[1])] += 1
        # 必要があれば max と min を更新する
        min_v = min(min_v,int(que[1]))
        max_v = max(max_v,int(que[1]))
    elif que[0] == "2":
        # que 2の時、dict から key xについて、valueを指定の数減らす
        del_num = min(int(que[2]),s[int(que[1])])
        s[int(que[1])] -= del_num
        if s[int(que[1])] == 0:
            # value が 0 になった場合、dict から削除する
            s.pop(int(que[1]))
            if len(s) == 0:
                # dict が空になったら、max と min を初期値に戻す
                min_v = 10**9+1
                max_v = 0
            else:
                # dict に値が残っていれば、max と min を更新する
                # 削除したやつが max or min だった場合、それぞれ max と min を設定し直す
                if min_v == int(que[1]):
                    min_v = min(s)
                if max_v == int(que[1]):
                    max_v = max(s)
    else:
        print(max_v-min_v)