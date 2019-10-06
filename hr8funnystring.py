def reverse_a_string(take_string):
    return take_string[::-1]

def find_funn_notfunny(take_string):
    l=len(take_string)
    arr1= [];
    arr2=[];
    for ch in take_string:
        arr1.append(ord(ch))
    string2 = reverse_a_string(take_string)
    for ch in string2:
        arr2.append(ord(ch))
    flag=0;
    for i in range(l-1):
        if abs((arr1[i+1]-arr1[i]))!=abs(arr2[i]-arr2[i+1]):
            flag=1;
        if flag==1:
            break;

    if flag==0:
        return "Funny"
    else:
        return "Not Funny"

if __name__ =="__main__":
    n=int(input());
    for i in range(n):
        input_str = input();
        print(find_funn_notfunny(input_str))