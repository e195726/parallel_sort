from multiprocessing import Pool
import random
import time

#並列計算させる関数(処理):引数1つ
#この場合は，クイックソート
def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr

    # データの状態に左右されないためにrandom.choice()を用いることもある。
    # ref = random.choice(arr)
    ref = arr[0]
    ref_count = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else:
            ref_count += 1
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right
numlist =[]

for i in range(1000):
    numlist.append(random.random())

arr = [numlist,numlist]


#並列計算させてみる
if __name__ == "__main__":
    p = Pool(4)
    t1 = time.time() 
    quick_sort(numlist)
    quick_sort(numlist)
    t2 = time.time() 

    t3 = time.time() 
    p.map( quick_sort, arr )#並列演算
    t4 = time.time() 
    elapsed_time = t2-t1
    print("逐次処理の"+f"経過時間：{elapsed_time}")
    elapsed_time = t4-t3
    print("並列処理の"+f"経過時間：{elapsed_time}")