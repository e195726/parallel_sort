from multiprocessing import Pool
import random
import time

#並列計算させる関数(処理):引数1つ
#この場合は，バブルソート
def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
    #print(arr)
    return arr

numlist =[]
for i in range(1000):
    numlist.append(random.random())

arr = [numlist,numlist]


#並列計算させてみる
if __name__ == "__main__":
    p = Pool(4)
    t1 = time.time() 
    bubble_sort(numlist)
    bubble_sort(numlist)
    t2 = time.time() 

    t3 = time.time() 
    p.map( bubble_sort, arr )#並列演算
    t4 = time.time() 
    elapsed_time = t2-t1
    print("逐次処理の"+f"経過時間：{elapsed_time}")
    elapsed_time = t4-t3
    print("並列処理の"+f"経過時間：{elapsed_time}")

    #https://qiita.com/suecharo/items/30f5d817da4c948c3be6
    #https://qiita.com/studio_haneya/items/1cf192a0185e12c7559b