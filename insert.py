from multiprocessing import Pool
import random
import time

#並列計算させる関数(処理):引数1つ
#この場合は，挿入ソート
def insert_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        ele = arr[i]
        while arr[j] > ele and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = ele
    return arr

numlist =[]
for i in range(1000):
    numlist.append(random.random())

arr = [numlist,numlist]


#並列計算させてみる
if __name__ == "__main__":
    p = Pool(4)
    t1 = time.time() 
    insert_sort(numlist)
    insert_sort(numlist)
    t2 = time.time() 

    t3 = time.time() 
    p.map( insert_sort, arr )#並列演算
    t4 = time.time() 
    elapsed_time = t2-t1
    print("逐次処理の"+f"経過時間：{elapsed_time}")
    elapsed_time = t4-t3
    print("並列処理の"+f"経過時間：{elapsed_time}")