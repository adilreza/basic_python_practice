def calculate_tallest(take_arry):
    result=0;
    take_arry.sort();

    for i in range(n-1,0,-1):
        if (take_arry[i-1]-take_arry[i])==0:
            result=result+1;
        else:
            break;
    return result+1;





n=0;
if __name__=="__main__":
    n = int(input())
    take_all_kandle = list(map(int, input().rstrip().split()))
    print(calculate_tallest(take_all_kandle))