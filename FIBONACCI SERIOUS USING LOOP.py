# WRITE A PYTHON PROGRAM TO GET THE FIBONACCI SERIES BETWEEN 0 TO 50 USING LOOP


a = 0
b = 1
c = 0
for number in range(10):         #USING FOR LOO[P]
    print(a)
    c = a+b
    b = a
    a = c

print("SAYAN's","ASSIGNMENT",sep="__",end="\n")
print("=============================================")
x,y =0,1
while y<50:
    print(y,)                     #USING WHILE LOOP
    x,y =y, x+y
print("=============================================")