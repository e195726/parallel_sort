from multiprocessing import Pool
import time
import make_list
import sellect
import merge
import quick
import insert
import count
import bubble
import sys
sys.setrecursionlimit(10000)



number_list=[10,100,1000,10000]
sort_list=[sellect,merge,quick,insert,count,bubble]
sort_list2=["sellect","merge","quick","insert","count","bubble"]

#並列計算させてみる
if __name__ == "__main__":
    for j in number_list:
        print(j)
        numlist=[make_list.make(j)]

        for i in range(len(sort_list)):
            t1 = time.time() 
            sort_list[i].sort(numlist[0])
            t2 = time.time() 
            elapsed_time = t2-t1
            print(sort_list2[i]+":逐次処理"+f"経過時間：{elapsed_time}")

        print("==================================")

        p = Pool(4)
        for i in range(len(sort_list)):
            t3 = time.time() 
            p.map(sort_list[i].sort,numlist)#並列演算
            t4 = time.time() 
            elapsed_time = t4-t3
            print(sort_list2[i]+":並列処理の"+f"経過時間：{elapsed_time}")

        print("==================================")


#https://qiita.com/suecharo/items/30f5d817da4c948c3be6
#https://qiita.com/studio_haneya/items/1cf192a0185e12c7559b