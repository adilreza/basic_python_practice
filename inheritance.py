class parent_class:
    a=4;
    b=3;
    def parent_fuction(self):
        print("this is from parent function")
        return 0;


class child_class(parent_class):#this way inherited
    def child_function(self):
        print("this is me from child function")

    def make_sum(self):
        sum = self.a+ self.b;
        return sum;


if __name__=="__main__":
    myobj = child_class()
    print(myobj.a)
    print(myobj.parent_fuction())
    print(myobj.make_sum())
