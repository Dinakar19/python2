def factorial(n):
   if not isinstance(n,int):
      raise RuntimeError("Argument must be int")
   if n<0:
      raise RuntimeError("arguments must be greater than 0")
   f=1
   for i in range(n):
      f*=n
      n-=1
      return f
try:
   print("facorial of 120 is:",factorial(5))
except RuntimeError:
   print("invalid input")
