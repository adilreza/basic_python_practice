
def picking_number(take_array):
    max=0;
    for i in range(n):
        cnt=0
        for j in range((i),(n)):
            if abs(take_array[i]-take_array[j])<=1:
                cnt=cnt+1;
            else:
                break;

        if cnt>max:
            max=cnt;
    return max;

n=0;
if __name__=="__main__":
    n=int(input())
    arr = list(map(int,input().rstrip().split()));
    arr.sort();
    print(picking_number(arr))

