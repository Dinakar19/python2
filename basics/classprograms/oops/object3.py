class student:
   def __init__(self,aname,arno,afee):
      self.name=aname
      self.rno=arno
      self.fee=afee
   def put_details(self):      
      print("The name is:",self.name)
      print("Roll no is:",self.rno)
      print("Fees is:",self.fee)
   def __del__(self):
      print("object is destroyed")
s1=student("john",450,50000)
#s1=student()
s2=student("abraham",450,47000)
print("first created object details")
s1.put_details()
print("second created object details")
s2.put_details()
