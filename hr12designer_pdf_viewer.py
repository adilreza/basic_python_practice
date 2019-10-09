def find_result(take_string):
    max=0;
    for i in range(0,n,1):
        ord_ascci = ord(take_string[i])-97;
        if(height_list[ord_ascci]>max):
            max=height_list[ord_ascci];
    return max;

n=0;
height_list=[];
if __name__=="__main__":
    height_list = list(map(int,input().rstrip().split()))
    get_in = input();
    n=len(get_in);
    get_max = find_result(get_in);
    print(n*get_max)
