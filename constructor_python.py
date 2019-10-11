class my_contructor_test_class:
    a=10;
    b=15;
    message ="This is single message";
    sum=0;
    def __init__(self):
        print("Hello I am from constuctor");
        self.sum=self.a+self.b;
    def mul_function(self,num1,num2):
        return num1*num2;



if __name__=="__main__":
    myobj1 = my_contructor_test_class();
    tak_in = input()
    result=myobj1.mul_function(10,20)
    print(myobj1.message)
    print(myobj1.sum)
    print(result)
