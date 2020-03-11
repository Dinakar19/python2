i=int(input("Enter a number:"))
sume=0
while i>0:
   temp=i%10
   sume=sume+temp
   i=i//10
print("sum=:",sume)
