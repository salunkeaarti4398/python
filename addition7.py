print("Application to demonstrate industrial programming")

def Addition(Value1,Value2):
    Ans = Value1 + Value2
    return Ans
def main():
    print("Enter First no.:")
    no1 = int(input())
    print("Enter Second no.:")
    no2 = int(input())

    Ret = Addition(no1,no2)


    print("Addition is :",Ret)

if __name__ == "__main__":
    main()

