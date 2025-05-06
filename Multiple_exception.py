try:
    num1 , num2=eval(input("enter 2 numbers seperated by a comma: "))
    result=num1/num2
    print("the result is ",result)

except ZeroDivisionError:
    print("division by zero results in an error")

except SyntaxError:
    print("comma is missing. the numbers entered should be seperated by a comma like 1,2")

except:
    print("wrong input")

else:
    print("no exceptions")

finally:
    print("this will execute no matter what")