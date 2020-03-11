class student:
   def get_details(self):
      self.name="john"
      self.rno=14
      self.fees=50000.00
   def put_details(self):
      print("Name is:",self.name)
      print("RNO is:",self.rno)
      print("Fee is:,",self.fees)
obj=student()
obj.get_details()
obj.put_details()
