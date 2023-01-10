
print("===========================================================",end="\n\n")

lst = eval(input('type a list...', ))                #  taking input from user......


#lst = [2,5,7,4,9]                                  # a Python program to square the elements of a list using map() function.
sayan = list(map(lambda x : x*x , lst))
print(end="\n\n")
print('SQUARED list is :' , sayan,end="\n\n")

print("===============================================SAYAN=======")