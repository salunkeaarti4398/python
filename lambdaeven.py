def CheckEven(No):
    if (No % 2 == 0):
        return True
    else :
        return false
def CheckEvenX(No):
    return(No % 2 == 0)

Ret = CheckEvenX(12)

if(Ret == True):
    print("Its Even")
else:
    print("Its odd")