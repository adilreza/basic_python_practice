def function_min_max(take_array):
    l=len(take_array)
    sum=0;
    mn=99999999999;
    mx=-99999999;
    for i in take_array:
        sum=sum+i;
        if i>mx:
            mx=i;
        if i<mn:
            mn=i;
    return (sum-mx), (sum-mn)

if __name__=="__main__":
    arr = list(map(int, input().rstrip().split()));
    arr.sort()
    a,b = function_min_max(arr);
    print("%d %d"%(a,b))