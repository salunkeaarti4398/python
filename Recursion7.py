
def Display(No):

    if(No <= 0):
        return 0
    else:

       return (No + Display(No - 1))

Ret = Display(4)
print("Result is :",Ret)
