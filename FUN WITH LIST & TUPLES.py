print("SAYAN's_ASSIGNMENT", end="\n\n")
print("=================================", end="\n\n")


lst = [(2,5), (1,2), (4,4), (2,3), (2,1)]

for i in range(len(lst)):
    for j in  range(len(lst)):
        if lst[i][1]<lst[j][1]:
            lst[i],lst[j]=lst[j],lst[i]

print(lst, end="\n\n")
print('===============================')
