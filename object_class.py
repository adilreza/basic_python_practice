class Myclass:
    a = 0;
    adil ="cse ruet";
    def hello_adil(self):
        print("Hello world");
        return "this is from hello_adil"
    def access_same_class(self):
        print(self.adil)


if __name__=="__main__":
    myobject = Myclass()
    adil = myobject.adil;
    print(adil)
    myobject.access_same_class()



