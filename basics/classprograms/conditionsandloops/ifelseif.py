a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>b and a>c:
   print("a is big:",a)
elif b>a and b>c:
   print("b is big:",b)
elif c>a and c>b:
   print("c is big:",c)
else:
   print("two or more numbers are equal")
