list1=[9,6,5,8,1,3,7,4]
print(list1)             #printing the complete list
print(list1[:-5])        #this will slice the elements from -5 to backward index
print(list1[-5:])         #this will slice the elements from -5 to forward index
print(list1[:5])         #this will siice the string from 5 to backward index
print(list1[5:])         #this will slice the string from 5 to forward index   
print(list1[2:5])        #this will slice the string in between 2;5 
print(list1[-5:-2])      #this will slice inbetween -5:-2
list1[2:5]=[11,12,14]    #modifying the elements between 2:5
print(list1)             #printing the complete list     
