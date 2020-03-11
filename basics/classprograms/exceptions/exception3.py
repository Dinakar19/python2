try:
   value1=int(input("enter a number1:"))
   value2=int(input("enter a number2:"))
   result=value1/value2
   print("result is:",result)
except ValueError:
   print("value error:exception handler")
   print("invalid input:only integers are allowed")
except ZeroDivisionError:
   print("zerodivisionerror:exception handler")
   print("ohh!!!can not divide a number by zero")
except IndentationError:
   print("indentation error:exception handler")
else:
   print("program successfully executed")

