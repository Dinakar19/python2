a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
# res=a/b
# print("result is:",res)
try:
   res=a/b
   print("result is:",res)
except ZeroDivisionError:
   print("ZeroDivisionError is making an exception")
print("after result")
