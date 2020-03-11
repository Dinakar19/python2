class student:
        def __init__(self,aname,arno,afee):
                self.name=aname
                self.rno=arno
                self.fee=afee
        def put_details(self):
                print("Name is:",self.name)
                print("Rno is",self.rno)
                print("Fee is:",self.fee)
        def __del__(self):
                print("Object destroyed")
obj_s1=student("dinakar",14,1000000)
#obj_s1=student()
obj_s2=student("mahesh",30,1000000)
print("Obect:1st Created Object Details")
obj_s1.put_details()
print("Obect:2nd Created Object Details")
obj_s2.put_details()
