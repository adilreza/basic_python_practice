
import  math

def get_answer(take_string, r, c,l):
    cnt=0;
    tch = "";
    matrix =[]
    for ch in take_string:
        tch=tch+ch;
        cnt=cnt+1;
        if cnt==c:
            cnt=0;
            matrix.append(tch)
            tch = "";
    if tch!="":
        matrix.append(tch)

    i=0;
    output_s="";
    for string_t in matrix:
        output_s=output_s+string_t;

    o_ch="";
    for i in range(0,c,1):
        o_ch = output_s[i];
        for j in range(i,l,c):
            if (c+j)<l:
                o_ch=o_ch+output_s[c+j]

        print(o_ch, end=" ")
        o_ch=""




if __name__=="__main__":
    input_string = input();
    input_string.replace(" ","");
    l = len(input_string);
    r = int(math.sqrt(l))
    c =r+1;
    if r*c<l:
        r=r+1;
    get_answer(input_string, r, c, l)
