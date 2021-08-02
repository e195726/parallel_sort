from multiprocessing import Pool
import random
import time

#並列計算させる関数(処理):引数1つ
#この場合は，バブルソート
def bucket_sort(arr):
    arrc = [0]*(max(arr)+1)

    #カウンタ配列の作成。0始まり。0番目は常に０
    for i in arr:
        arrc[i] += 1
    #ソート結果を入れる配列を用意
    ans=[]
    for j in range(1, len(arrc)):
        ans.extend([j]*arrc[j])
    return ans


numlist =[]
for i in range(1000):
    numlist.append(random.randint(0,1000))

arr = [numlist,numlist]


#並列計算させてみる
if __name__ == "__main__":
    p = Pool(4)
    t1 = time.time() 
    bucket_sort(numlist)
    bucket_sort(numlist)
    t2 = time.time() 

    t3 = time.time() 
    p.map( bucket_sort, arr )#並列演算
    t4 = time.time() 
    elapsed_time = t2-t1
    print("逐次処理の"+f"経過時間：{elapsed_time}")
    elapsed_time = t4-t3
    print("並列処理の"+f"経過時間：{elapsed_time}")

    #https://qiita.com/suecharo/items/30f5d817da4c948c3be6
    #https://qiita.com/studio_haneya/items/1cf192a0185e12c7559b