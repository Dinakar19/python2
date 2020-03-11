empdetails={
    "name":"Dinakar",
     "id": 14,
     "salary":1000000.00
}
print(empdetails)
print(empdetails['name'])
print("***********************************")
print("length is:",len(empdetails))
print("***********************************")
sta="name" in empdetails
print("sta is:",sta)
sta1="Din" not in empdetails
print("sta1 is:",sta1)
print("***********************************")
print(empdetails.keys())
print("*************************************")
print(empdetails.values())
print("***********************************")
print(empdetails.items())
print("************************************")
print(empdetails.get('name'))
print("*************************************")
print(empdetails.pop('name'))
print("**************************************")
print(empdetails.popitem())
copy_empdetails=empdetails.copy()
print("**************************************")
print(copy_empdetails)
copy_empdetails.clear()
print("**************************************")
print(copy_empdetails)
