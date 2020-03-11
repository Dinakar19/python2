f=open('file.txt','w')
f.write('hello world\n')
f.write('hi how are you\n')
f.write('fine whats going on\n')
f=open('file.txt','r')
contents=f.readlines()
for line in contents:
   print(line)
