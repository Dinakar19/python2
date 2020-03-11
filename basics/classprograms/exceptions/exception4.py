try:
   value1=int(input("enter a number:"))
   value2=int(input("enter a number:"))
   result=value1/value2
   print("result is:",result)
except ValueError:
   print("valueerror:exception handler")
   print("invalid input:only integers are allowed")
except ZeroDivisionError:
   print("zerodivision error:exception handler")
   print("ohh!!! can  divide a number by zero")
except IndentationError:
   print("indentation error: exception handler")
finally:
   print("this is final clause")
