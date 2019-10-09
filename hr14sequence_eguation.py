if __name__=="__main__":
    n = int(input());
    take_arr = list(map(int, input().rstrip().split()))
    arr2index=[]
    for i in range(1,n+1,1):
        arr2index.append(take_arr.index(i)+1)
    for j in range(0,n,1):
        print(take_arr.index(arr2index[j])+1)