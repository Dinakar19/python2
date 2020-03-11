import os
filename=input("enter file name")
try:
   f=open(filename,"r")
   for line in f:
      print(line,end="")
   f.close()
except FileNotFoundError:
   print("file not found")
except PermissionError:
   print("Dont have the permission to open the file") 
except FileExistsError:
   print("dont have the permission to read the file")
except:
   print("unexpected error while reading the file")
else:
   print("program runned with out any probem")
finally:
   print("finally:this will always execute")
