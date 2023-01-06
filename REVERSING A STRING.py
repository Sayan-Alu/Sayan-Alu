

# =========================================================================================
#  WRITE A PYTHON PROGRAM THAT ACCEPT A WORD FROM THE USER AND REVERSE IT AS  THE OUTPUT
# =========================================================================================


a = str(input("type a string :" ))

print(f"after reversing --  {a[-1::-1]}")    # ======================== USE OF DOUBLE COLONS (::)  ==========================================

                                             # THIS DOUBKE COLONS USED FOR JUMPING OF ELEMENTS IN MULTIPLE AXES . IT IS ALSO A SLICE OPERATOR
                                             # EVERY ITEM OF THE SEQUENCE GETS SLICED USING DOUBLE COLONS
                                             # ===================================================================================================



b = str(input("type a string :" ))
print("after reversing . . . .", end="\n")      #  ==================================================================
for i in range((len(b)-1),-1,-1):               #          REVERSING THE STRING USING FOR LOOP AND INDEX CONCEPT
    print(b[i],end="")                          #  ==================================================================




