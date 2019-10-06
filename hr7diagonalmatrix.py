rc = 0;

def findresult(take_matrix):
    sum1=0;
    sum2=0;
    for i in range(rc):
        for j in range(rc):
            if i==j:
                sum1=sum1+matrix[i][j];
            if i+j==(rc-1):
                sum2=sum2+matrix[i][j];

    return abs(sum2-sum1)

matrix = []

if __name__ =="__main__":
    rc = int(input())
    for i in range(rc):
        rowinput = list(map(int, input().rstrip().split()))
        matrix.append(rowinput)

    print(findresult(matrix))