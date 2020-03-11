class student:
   database="student"
   def get_details(self,aname,arno,afee):
      self.name=aname
      self.rno=arno
      self.fee=afee
   def put_details(self):
      print("name is",self.name)
      print("Rno is:",self.rno)
      print("fee is:",self.fee)
      print("Database is:",self.database)
s1=student()
s2=student()
print("object:1st created object details")
s1.get_details("john",425,42000.0)
s1.put_details()
print("database is:",student.database)
print("object:2nd created object details")
s2.get_details("dinakar",140,5000.0)
s2.put_details()
print("*********after student database*********")
s1.database="john"
print("object:1st object details")
s1.put_details()
print("object:2nd object details")
s2.put_details()
