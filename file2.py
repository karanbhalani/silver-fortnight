hello = input()
print (hello) 
fd = "file3.py"
wr = "file4.py"
file = open(fd,'w')
file.write(hello)
file.close()
file = open(fd,'r')
text=file.read()
print(text)
file=open(wr,'w')
file.write(text)
file.close()
