


if __name__=="__main__":
    n=int(input());
    for i in range(n):
        all_input = list(map(int, input().rstrip().split()));
        diff1 = abs(all_input[0]-all_input[2])
        diff2 = abs(all_input[1]-all_input[2])
        if diff1>diff2:
            print("Cat B")
        elif diff1<diff2:
            print("Cat A")
        else:
            print("Mouse C")