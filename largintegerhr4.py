
def getsum(all_no):
    sum=0;
    for i in all_no:
        sum=sum+i;
    return sum;

n = int(input());
all_no = list(map(int, input().rstrip().split()));

print(getsum(all_no))