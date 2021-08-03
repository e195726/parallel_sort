#並列計算させる関数(処理):引数1つ
#この場合は，カウントソート
def sort(arr):
    arrc = [0]*(max(arr)+1)

    #カウンタ配列の作成。0始まり。0番目は常に０
    for i in arr:
        arrc[i] += 1
    #ソート結果を入れる配列を用意
    ans=[]
    for j in range(1, len(arrc)):
        ans.extend([j]*arrc[j])
    return ans