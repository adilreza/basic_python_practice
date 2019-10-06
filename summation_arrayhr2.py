def show_ooutput(take_array):
    sum=0;
    for i in take_array:
        sum=sum+i;
    return sum;

arr = [];
if __name__ =="__main__":
    n=int(input())
    arr = list(map(int,input().split()))# in this way the input is taken from user by space separated
print(show_ooutput(arr))