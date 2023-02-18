
def Display(No):
    cnt = 0
    while(No > 0):
        cnt = cnt + No
        No = No - 1

    return cnt



Ret = Display(4)
print("Result is :",Ret)
