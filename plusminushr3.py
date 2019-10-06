def adder(arr_v):
    ev=0; zero=0; odd=0;
    l=len(arr_v)
    for i in arr_v:
        if(i>0):
            ev=ev+1;
        elif i==0:
            zero=zero+1;
        else:
            odd=odd+1;

    r1=float(ev/l);
    r2=float(zero/l);
    r3=float(odd/l);

    print("%.6f"%(r1));
    print("%.6f"%(r3));
    print("%.6f"%(r2));
if __name__ =="__main__":
    n = int(input())
    arr = list(map(int, input().strip().split()));
    adder(arr)
