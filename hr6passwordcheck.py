
def find_error(take_string):
    l=len(take_string)
    no_error = 0;
    flag1=flag2=flag3=flag4=0;
    for ch in take_string:
        if(ch>="0" and ch<="9"):
            if flag1==0:
                no_error=no_error+1;
                flag1=1;
        elif ch>="a" and ch<="z":
            if flag2==0:
                no_error=no_error+1;
                flag2=1;
        elif ch>="A" and ch<="Z":
            if flag3==0:
                no_error=no_error+1;
                flag3=1;
        else:
            if flag4==0:
                no_error=no_error+1
                flag4=1;
    unsatisfied = 4-no_error;
    if l<6:
        answer = unsatisfied;
        l=l+unsatisfied;
        if l<6:
            answer=answer+(6-l);
    else:
        answer = unsatisfied
    return answer;


if __name__=="__main__":
    n = int(input());
    get_str = input();
    print(find_error(get_str))
