def default_args_fun(a=10,b=20,c=30):
   print("the value a is:",a)
   print("the value b is:",b)
   print("the value c is:",c)
x=1
y=2
z=3
print("calling with out args")
print("\n")
default_args_fun()
print("calling with two args")
print("\n")
default_args_fun(x)
print("calling with two args")
print("\n")
default_args_fun(x,y)
print("calling with two args")
print("\n")
default_args_fun(x,z)
print("calling with three args")
print("\n")
default_args_fun(x,y,z)
print("\n")
print("\n")
print("***********************************************")