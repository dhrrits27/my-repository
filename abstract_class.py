class Abclass():
    
    def print(self,x):
        print("passed value:",x)

    def task(self):
        print("we are inside Abclass")

class test_class(Abclass):

    def task(Self):
        print("we are inside test_class task")

test_obj=test_class()
test_obj.task()
test_obj.print(100)

