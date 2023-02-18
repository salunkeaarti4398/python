print("Application to demonstrate industrial programming")

import marvellousmodule

def main():
    print("Value of __name__from main is :",__name__)
    print("Enter First no.:")
    no1 = int(input())
    print("Enter Second no.:")
    no2 = int(input())

    Ret = marvellousmodule.Addition(no1,no2)


    print("Addition is :",Ret)

if __name__ == "__main__":
    main()

