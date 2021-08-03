from multiprocessing import Pool
import time
import make_list
import sellect
import merge
import quick
import insert
import count
import bubble


numlist=[make_list.make()]

#並列計算させてみる
if __name__ == "__main__":
    p = Pool(4)
    t1 = time.time() 
    sellect.sort(numlist)
    merge.sort(numlist)
    quick.sort(numlist)
    insert.sort(numlist)
    count.sort(make_list.make())
    bubble.sort(numlist)
    t2 = time.time() 

    t3 = time.time() 
    p.map(sellect.sort,numlist)#並列演算
    p.map(merge.sort,numlist)
    p.map(quick.sort,numlist)
    p.map(insert.sort,numlist)
    p.map(count.sort,numlist)
    p.map(bubble.sort,numlist)

    t4 = time.time() 
    elapsed_time = t2-t1
    print("逐次処理の"+f"経過時間：{elapsed_time}")
    elapsed_time = t4-t3
    print("並列処理の"+f"経過時間：{elapsed_time}")


#https://qiita.com/suecharo/items/30f5d817da4c948c3be6
#https://qiita.com/studio_haneya/items/1cf192a0185e12c7559b