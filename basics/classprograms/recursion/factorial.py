def calc_factorial(x):
   if x==1:
      return 1
   else:
      return(x*calc_factorial(x-1))
num=int(input("Enter a number:"))
fact=calc_factorial(num)
print(fact)
