try:
   value1=int(input("Enter number1:"))
   value2=int(input("Enter number2:"))
   result=value1/value2
   print("resultis:",result)
except ValueError:
   print("value error:exception handler")
   print("invalid input:only integers are allowed")
except ZeroDivisionError:
   print("ZeroDivisionError:exception handler")
   print("ohh!!!cant divide a number by zero")
except IndentationError:
   print("IndentationError:exception handler")
print("after exception")
