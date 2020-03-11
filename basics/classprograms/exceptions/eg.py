res=0
try:
   a=int(input("Enter 1st no:"))
   b=int(input("Enter 2nd no:"))
   res=a//b
   print(res)
except ZeroDivisionError:
   print("can not divide a number by zero")
print("\n*************************")
print("program terminated")
c=res+1
print(c)  
