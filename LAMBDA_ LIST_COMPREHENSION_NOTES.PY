


def subtracting_5(num):
  #num = num - 5
  return num - 5
 
print(subtracting_5(10))

subtracting_5_new = lambda num : num - 5
# lambda <paramter> : <expressions> 
print(subtracting_5_new(10))


multiply_two_nos = lambda x,y : x*y
print(multiply_two_nos(10,20))

def multi(a,c):
    b = a*c
    return b

def maximum(a,b):
    if a>b:
        return a
    else:
        return b
    
print(maximum(100,50))   

maximum_new = lambda a,b : a if a>b else b
print(maximum_new(100,50))  
    
    
# lambda <parameters> : <if Expression>
# <if Expression> --> TRUE if condition else FALSE


text_list_final = []
text_list = ["lists","are","IMPORTANT","data","TYPE"]
def to_make_uppercase(text_list):
    for word in text_list:
        if word.islower():
            text_list_final.append(word.upper())
        else:
            text_list_final.append(word.lower())
    return text_list_final
    
print(to_make_uppercase(text_list))



final_list_comp = [word.upper() if word.islower() else word.lower() for word in text_list]







a,b,c = "abc","pqr","xyz"
print(a, b, c)
print(a+b+c)
print(a+" -- "+b+" -- "+c)
print(f"{a} -- {b} -- {c}")
print(f"asd asd asd {maximum_new(1000,150)}")
# f" asdasda {variable} aasasdasda"



list_new = [1,2,3]
list_final=[]

def squaring_list(list_param):
    for i in list_param:
        list_final.append(i*i)
    return list_final

print(squaring_list(list_new)) #[1,4,9]

# map(func,iteratable)

print("lambda ", list(map(lambda x:x*x, list_new)))




list_new = [1,2,3]
list_final=[]
def add_5(list_param):
    for i in list_param:
        list_final.append(i+5)
    print(list_final) # [6,7,8]
    
    
add_5(list_new)

print([i+5 for i in list_new])



text_list_final = []
text_list = ["lists","are","IMPORTANT","data","TYPE"]
def to_make_uppercase(text_list):
    for word in text_list:
        if word.islower():
            text_list_final.append(word.upper())
        else:
            text_list_final.append(word.lower())
    return text_list_final
    
print(to_make_uppercase(text_list))



final_list_comp = [word.upper() if word.islower() else word.lower() for word in text_list]