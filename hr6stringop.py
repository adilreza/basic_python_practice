
def counter(tak_string):
    cnt=0;
    for ch in tak_string:
        if ch>="A" and ch<="Z":
            cnt+=1;

    return cnt+1;



if __name__=='__main__':
    input_str = input();
    print(counter(input_str))