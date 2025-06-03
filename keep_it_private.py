class myClass:

    __privateVar=27;

    def __privMeth(self):
        print("im inside myClass")

    def hello(self):
        print("private variable value: ",myClass.__privateVar)
        myClass.__privMeth(self)

foo=myClass()
foo.hello()

